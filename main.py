from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from httpx import AsyncClient
from api.DiscworldClient import DiscworldClient
from views.person_list import render_person_list
from views.person_detail import render_person_detail
from models.discworld import ApiSampleProjectPersonListParametersQuery

app = FastAPI()

http_client = AsyncClient(follow_redirects=True) # TODO: close on shutdown
api = DiscworldClient(http_client, base_url="https://discworld.acdh-dev.oeaw.ac.at/")

@app.get("/persons/", response_class=HTMLResponse)
async def list_persons(request: Request):
    # accept same query params as the api
    params = ApiSampleProjectPersonListParametersQuery.model_validate(request.query_params)

    person_list = await api.get_person_list(params)
    if person_list is None:
        return HTMLResponse(status_code=404)
    
    return render_person_list(person_list)

@app.get("/persons/{url:path}", response_class=HTMLResponse)
async def get_person(url: str):
    person = await api.get_person_detail(url)
    if person is None:
        return HTMLResponse(status_code=404)
    
    return render_person_detail(person)