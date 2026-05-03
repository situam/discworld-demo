from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from httpx import AsyncClient
from api.DiscworldClient import DiscworldClient
from views.person_list import render_person_list

app = FastAPI()

http_client = AsyncClient(follow_redirects=True) # TODO: close on shutdown
api = DiscworldClient(http_client, base_url="https://discworld.acdh-dev.oeaw.ac.at/")

@app.get("/persons/", response_class=HTMLResponse)
async def list_persons():
    person_list = await api.get_person_list()
    if person_list is None:
        return HTMLResponse(status_code=404)
    
    return render_person_list(person_list)

@app.get("/persons/{person_id}", response_class=HTMLResponse)
async def get_person(person_id: int):
    return f"<pre>get_person with id: {person_id}</pre>"