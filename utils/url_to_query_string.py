from pydantic import AnyUrl
from urllib.parse import urlsplit


def url_to_query_string(url: AnyUrl) -> str:
    q = urlsplit(str(url)).query
    return f"?{q}" if q else ""
