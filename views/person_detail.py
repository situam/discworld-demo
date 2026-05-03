from models.views import ExpandedPersonView
from views.dict import render_dict_dl

def render_expanded_person_view(
    data: ExpandedPersonView
):
    return f"""
<html>
    <head>
        <title>Person: {data.fullname}</title>
    </head>
    <body>
        <h1>Person: {data.fullname}</h1>
        {render_dict_dl(data.to_dict())}
    </body>
</html>
"""