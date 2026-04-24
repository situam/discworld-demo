from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/persons/", response_class=HTMLResponse)
async def list_persons():
    return "<pre>list persons</pre>"

@app.get("/persons/{person_id}", response_class=HTMLResponse)
async def get_person(person_id: int):
    return f"<pre>get_person with id: {person_id}</pre>"