## Dependencies

- FastAPI
- datamodel-code-generator
- Pydantic 

## Local Development

### 1. Install dependencies
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Generate Discworld models from OpenAPI

1. Download schema:

```sh
curl -s https://discworld.acdh-dev.oeaw.ac.at/swagger/schema/ > discworld/schema.yaml
```

2. Generate models

```sh
datamodel-codegen --use-operation-id-as-name --input discworld/schema.yaml --input-file-type openapi --openapi-scopes schemas parameters paths --output-model-type pydantic_v2.BaseModel --output models/discworld.py
```

## Start dev server:

```sh
fastapi dev
```