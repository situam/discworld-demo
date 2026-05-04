from typing import Type, TypeVar
from pydantic import BaseModel
import httpx
import asyncio

T = TypeVar("T", bound=BaseModel)


async def get_model(
    http_client: httpx.AsyncClient,
    url: str,
    model: Type[T],
    params: BaseModel | None = None,
) -> T | None:
    """
    Fetch a JSON resource and parse into a Pydantic model

    returns None if response not 200
    raises ValidationError on invalid response
    """

    query_params = params.model_dump(exclude_none=True) if params is not None else None

    res = await http_client.get(
        url, headers={"Accept": "application/json"}, params=query_params
    )

    if res.status_code != 200:
        return None

    return model.model_validate_json(res.content)


async def get_models(
    http_client: httpx.AsyncClient,
    urls: set[str],
    model: Type[T],
):
    results = await asyncio.gather(
        *(get_model(http_client, url, model) for url in urls)
    )

    return dict(zip(urls, results))
