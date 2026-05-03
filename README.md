# Discworld Demo

Provides expanded views of discworld person data from [https://discworld.acdh-dev.oeaw.ac.at/](https://discworld.acdh-dev.oeaw.ac.at/)

## Dependencies

- FastAPI
- datamodel-code-generator

## Local Development

### Install dependencies
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Start dev server:

```sh
fastapi dev
```

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