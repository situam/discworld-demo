from models.discworld import (
    PaginatedPersonlistModelList,
    PersonlistModel
)

# TODO: pagination

def render_person_list(
    person_list: PaginatedPersonlistModelList,
):  
    return f"""<html>
<head>
    <title>Persons</title>
</head>
<body>
    <h1>Persons</h1>

    <table>
        <thead>
            {person_header_row}
        </thead>
        <tbody>
            {"".join(
                render_person_row(p) for p in person_list.results
            )}
        </tbody>
    </table>
</body>
</html>"""

person_header_row = """<tr>
    <th>surname</th>
    <th>forename</th>
    <th>gender</th>
    <th>date of birth</th>
    <th>date of death</th>
    <th>profession</th>
    <th>url</th>
</tr>"""

def render_person_row(person: PersonlistModel):
    return f"""<tr>
    <td>{str(person.surname)}</td>
    <td>{str(person.forename)}</td>
    <td>{str(person.gender)}</td>
    <td>{person.date_of_birth or ""}</td>
    <td>{person.date_of_death or ""}</td>
    <td>{person.profession}</td>
    <td>{person.url}</td>
</tr>"""