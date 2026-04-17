# Recommended Stacks

Pre-tested package combinations for common Azure Functions project types.

Each stack lists the toolkit packages to install, what they provide together,
and the scaffold command to generate a matching project.

## API Stack

**Best for:** REST APIs, webhooks, and public-facing HTTP services.

| Package | Role |
|---------|------|
| `azure-functions-openapi-python` | Swagger UI + OpenAPI 3.1 spec |
| `azure-functions-validation-python` | Pydantic request/response validation |
| `azure-functions-logging-python` | Structured JSON logging |

```bash
afs new my-api --profile api
```

```text
# requirements.txt
azure-functions
azure-functions-openapi-python
azure-functions-validation-python
azure-functions-logging-python
```

**What you get:** validated HTTP endpoints with auto-generated API docs,
structured logs, and request correlation IDs.

---

## DB API Stack

**Best for:** CRUD APIs backed by PostgreSQL, MySQL, or SQL Server.

| Package | Role |
|---------|------|
| `azure-functions-openapi-python` | Swagger UI + OpenAPI 3.1 spec |
| `azure-functions-validation-python` | Pydantic request/response validation |
| `azure-functions-db-python` | Declarative database input/output bindings |
| `azure-functions-logging-python` | Structured JSON logging |

```bash
afs new my-api --profile db-api
```

```text
# requirements.txt
azure-functions
azure-functions-openapi-python
azure-functions-validation-python
azure-functions-db-python[postgres]
azure-functions-logging-python
```

**What you get:** everything in the API Stack plus declarative database
read/write bindings via `@db.input()` and `@db.output()`.

---

## AI Agent Stack

**Best for:** LangGraph-based conversational agents and AI workflows.

| Package | Role |
|---------|------|
| `azure-functions-langgraph-python` | LangGraph HTTP deployment adapter |
| `azure-functions-openapi-python` | Swagger UI for agent endpoints |
| `azure-functions-logging-python` | Structured JSON logging |

```bash
afs new my-agent --template langgraph
```

```text
# requirements.txt
azure-functions
langgraph
azure-functions-langgraph-python
azure-functions-openapi-python
azure-functions-logging-python
```

**What you get:** invoke, stream, and health endpoints for LangGraph graphs,
plus API documentation and structured logging.

---

## Full Stack

**Best for:** production applications that need everything — validated APIs,
database access, health diagnostics, and observability.

| Package | Role |
|---------|------|
| `azure-functions-openapi-python` | Swagger UI + OpenAPI 3.1 spec |
| `azure-functions-validation-python` | Pydantic request/response validation |
| `azure-functions-db-python` | Declarative database bindings |
| `azure-functions-logging-python` | Structured JSON logging |
| `azure-functions-doctor-python` | Pre-deploy diagnostic checks |

```bash
afs new my-api --profile db-api --with-doctor
```

```text
# requirements.txt
azure-functions
azure-functions-openapi-python
azure-functions-validation-python
azure-functions-db-python[postgres]
azure-functions-logging-python
azure-functions-doctor-python
```

**What you get:** a fully instrumented API with validation, database access,
API docs, structured logging, and pre-deploy health diagnostics.

---

## Choosing a Stack

| Stack | Scaffold Command | Packages | Use Case |
|-------|-----------------|----------|----------|
| API | `afs new my-api --profile api` | 3 | REST APIs, webhooks |
| DB API | `afs new my-api --profile db-api` | 4 | CRUD with database |
| AI Agent | `afs new my-agent --template langgraph` | 3 | LangGraph agents |
| Full | `afs new my-api --profile db-api --with-doctor` | 5 | Production services |

Start with the smallest stack that covers your needs.
Add packages incrementally — the toolkit is designed for zero coupling between packages.
