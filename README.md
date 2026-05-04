# Discworld Demo

Provides expanded views of discworld person data from [https://discworld.acdh-dev.oeaw.ac.at/](https://discworld.acdh-dev.oeaw.ac.at/)

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

Open http://localhost:8000 in a web browser and start exploring

---

### Generate models from OpenAPI

1. Download schema:

```sh
wget -O discworld/schema.yaml https://discworld.acdh-dev.oeaw.ac.at/swagger/schema/
```

2. Generate models

```sh
datamodel-codegen --use-operation-id-as-name --input discworld/schema.yaml --input-file-type openapi --openapi-scopes schemas parameters paths --output-model-type pydantic_v2.BaseModel --output models/discworld.py
```