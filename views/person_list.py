from models.views import ExpandedPersonListView
from models.discworld import PersonlistModel, ProfessionlistModel
from views.pagination import render_pagination


def render_expanded_person_list(view: ExpandedPersonListView):
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
    <td>{str(person.surname)}</td>
    <td>{str(person.forename)}</td>
    <td>{str(person.gender)}</td>
    <td>{person.date_of_birth or ""}</td>
    <td>{person.date_of_death or ""}</td>
    <td>{", ".join(professions[str(url)].name for url in (person.profession or []))}</td>
    <td><a href='{href_detail}'>{person.url}</a></td>
</tr>"""
