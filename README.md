# Discworld Demo

Views of expanded discworld person data from [https://discworld.acdh-dev.oeaw.ac.at/](https://discworld.acdh-dev.oeaw.ac.at/).

Endpoints:

- `/persons`: paginated list view
  - filter by:
    - surname
    - forename
  - expanded: profession
- `/persons/{person.url}`: detail view
  - expanded: profession

A hosted instance is available at [https://discworld-demo.onrender.com/](https://discworld-demo.onrender.com/)

## Dependencies

- FastAPI
- datamodel-code-generator

## Running locally

### Install dependencies

Using uv:
```sh
uv sync
```

### Start server

```sh
uv run fastapi dev
```

Open `http://localhost:8000` in a web browser and start exploring

---

### Generate models from OpenAPI

1. Download schema:

```sh
wget -O schemas/discworld.yaml https://discworld.acdh-dev.oeaw.ac.at/swagger/schema/
```

2. Generate models

```sh
uv run datamodel-codegen
```