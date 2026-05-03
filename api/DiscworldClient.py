
from httpx import AsyncClient
from utils.get_model import get_model, get_models
from models.discworld import (
    ApiSampleProjectPersonListParametersQuery,
    PaginatedPersonlistModelList,
    PersondetailModel,
    ProfessionlistModel,
)
from models.views import ExpandedPersonView
from pydantic import AnyUrl

class DiscworldClient:
    def __init__(self, http_client: AsyncClient, base_url: str):
        self.http_client = http_client
        self.base_url = base_url

    async def get_person_list(self, params: ApiSampleProjectPersonListParametersQuery):
        return await get_model(
            http_client=self.http_client,
            url=self.base_url + "/api/sample_project.person/",
            model=PaginatedPersonlistModelList,
            params=params
        )
    
    async def get_person_detail(self, url: str):
        return await get_model(
            http_client=self.http_client,
            url=url,
            model=PersondetailModel
        )
    
    async def get_person_detail_expanded(self, url: str):
        person = await self.get_person_detail(url)
        if not person:
            return None

        professions = await self._expand_professions(person.profession or [])

        return ExpandedPersonView(person, professions)
    
    async def _expand_professions(self, urls: list[AnyUrl]):
        # deduplicate
        url_set = set(str(url) for url in urls)
        return await get_models(self.http_client, url_set, ProfessionlistModel)
