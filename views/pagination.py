def render_pagination(
    href_prev: str | None,
    href_next: str | None,
):
    return f"""
<nav>
    {f"<a href='{href_prev}'>&larr; previous page</a>" if href_prev else ""}
    {" | " if (href_prev and href_next) else ""}
    {f"<a href='{href_next}'>next page &rarr;</a>" if href_next else ""}
</nav>
    """