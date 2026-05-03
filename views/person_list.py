from models.discworld import (
    PaginatedPersonlistModelList,
    PersonlistModel
)
from views.pagination import render_pagination
from utils.url_to_query_string import url_to_query_string

# TODO: pagination

def render_person_list(
    person_list: PaginatedPersonlistModelList,
):  
    # pagination links: extract just the query string from the prev/next urls 
    link_to_prev_page = None if person_list.previous is None else url_to_query_string(person_list.previous)
    link_to_next_page = None if person_list.next is None else url_to_query_string(person_list.next)

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
    {render_pagination(
        href_prev=link_to_prev_page,
        href_next=link_to_next_page
    )}
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
    href_detail = f"/persons/{person.url}"

    return f"""<tr>
    <td>{str(person.surname)}</td>
    <td>{str(person.forename)}</td>
    <td>{str(person.gender)}</td>
    <td>{person.date_of_birth or ""}</td>
    <td>{person.date_of_death or ""}</td>
    <td>{person.profession}</td>
    <td><a href='{href_detail}'>{person.url}</a></td>
</tr>"""