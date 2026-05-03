
from httpx import AsyncClient
from utils.get_model import get_model
from models.discworld import PaginatedPersonlistModelList

class DiscworldClient:
    def __init__(self, http_client: AsyncClient, base_url: str):
        self.http_client = http_client
        self.base_url = base_url

    async def get_person_list(self):
        return await get_model(
            http_client=self.http_client,
            url=self.base_url + "/api/sample_project.person/",
            model=PaginatedPersonlistModelList
        )
