from models.discworld import PersondetailModel
from views.dict import render_dict_dl

def render_person_detail(
    person: PersondetailModel,
) -> str:
    fullname = f"{person.forename} {person.surname}"

    return f"""
<html>
    <head>
        <title>Person: {fullname}</title>
    </head>
    <body>
        <h1>Person: {fullname}</h1>
        {render_dict_dl(person.model_dump())}
    </body>
</html>
"""