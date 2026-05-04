from models.views import ExpandedPersonListView
from models.discworld import (
    ApiSampleProjectPersonListParametersQuery,
    PersonlistModel,
    ProfessionlistModel,
)
from views.pagination import render_pagination


def render_expanded_person_list(
    view: ExpandedPersonListView, params: ApiSampleProjectPersonListParametersQuery
):
    return f"""<html>
<head>
    <title>Persons</title>
</head>
<body>
    <h1>Persons</h1>

    {_render_filter(params)}
    <hr>
    <table>
        <thead>
            {person_header_row}
        </thead>
        <tbody>
            {
        "".join(
            render_person_row(p, view.professions) for p in view.person_list.results
        )
    }
        </tbody>
    </table>
    <hr>
    {
        render_pagination(
            href_prev=view.link_to_prev_page, href_next=view.link_to_next_page
        )
    }
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


def render_person_row(
    person: PersonlistModel, professions: dict[str, ProfessionlistModel | None]
):
    href_detail = f"/persons/{person.url}"

    return f"""<tr>
    <td>{person.surname}</td>
    <td>{person.forename}</td>
    <td>{person.gender}</td>
    <td>{person.date_of_birth or ""}</td>
    <td>{person.date_of_death or ""}</td>
    <td>{", ".join(professions[str(url)].name for url in (person.profession or []))}</td>
    <td><a href='{href_detail}'>{person.url}</a></td>
</tr>"""


def _render_filter(params: ApiSampleProjectPersonListParametersQuery):
    details_attrs = "open" if (params.surname or params.forename) else ""
    return f"""
<details {details_attrs}>
    <summary>filter</summary>
    <form method="GET">    
        <label>
            surname:
            <input type="text" name="surname" value="{params.surname or ""}">
        </label>
        <label>
            forename:
            <input type="text" name="forename" value="{params.forename or ""}">
        </label>
        <button type="submit">apply</button>
    </form>
</details>
"""
