
from httpx import AsyncClient
from utils.get_model import get_model
from models.discworld import (
    ApiSampleProjectPersonListParametersQuery,
    PaginatedPersonlistModelList,
    PersondetailModel,
)

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
