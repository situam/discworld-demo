from httpx import AsyncClient
from utils.get_model import get_model, get_models
from models.discworld import (
    ApiSampleProjectPersonListParametersQuery,
    PaginatedPersonlistModelList,
    PersondetailModel,
    ProfessionlistModel,
)
from models.views import ExpandedPersonView, ExpandedPersonListView
from pydantic import AnyUrl
from collections.abc import Iterable


class DiscworldClient:
    def __init__(self, http_client: AsyncClient, base_url: str):
        self.http_client = http_client
        self.base_url = base_url

    async def get_person_list(self, params: ApiSampleProjectPersonListParametersQuery):
        return await get_model(
            http_client=self.http_client,
            url=self.base_url + "/api/sample_project.person/",
            model=PaginatedPersonlistModelList,
            params=params,
        )

    async def get_person_list_expanded(
        self, params: ApiSampleProjectPersonListParametersQuery
    ):
        person_list = await self.get_person_list(params)
        if not person_list:
            return None

        # collect all linked professions
        profession_urls: set[AnyUrl] = set()
        for person in person_list.results:
            for url in person.profession or []:
                profession_urls.add(url)

        professions = await self._expand_professions(profession_urls)
        return ExpandedPersonListView(person_list, professions)

    async def get_person_detail(self, url: str):
        return await get_model(
            http_client=self.http_client, url=url, model=PersondetailModel
        )

    async def get_person_detail_expanded(self, url: str):
        person = await self.get_person_detail(url)
        if not person:
            return None

        professions = await self._expand_professions(person.profession or [])

        return ExpandedPersonView(person, professions)

    async def _expand_professions(self, urls: Iterable[AnyUrl]):
        # deduplicate
        url_set = set(str(url) for url in urls)
        return await get_models(self.http_client, url_set, ProfessionlistModel)
