from typing import Type, TypeVar
from pydantic import BaseModel
import httpx

T = TypeVar("T", bound=BaseModel)

async def get_model(
    http_client: httpx.AsyncClient,
    url: str,
    model: Type[T],
) -> T | None:
    """
    Fetch a JSON resource and parse into a Pydantic model

    returns None if response not 200
    raises ValidationError on invalid response
    """
    
    res = await http_client.get(
        url,
        headers={"Accept": "application/json"},
    )

    if res.status_code != 200:
        return None

    return model.model_validate_json(res.content)