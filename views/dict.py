def render_dict_dl(data: dict) -> str:
    return f"""<dl>
    {"".join(f"<dt>{key}</dt><dd>{value}</dd>" for key, value in data.items())}
</dl>"""
