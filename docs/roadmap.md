# Roadmap

## Phase 1: MVP

Status: implemented

Delivered:

- `new` command
- embedded HTTP scaffold
- Jinja2-based rendering
- repository tests for CLI behavior
- generated project quality baseline with `pytest` and `ruff`

## Phase 2: Guided Scaffolding

Status: implemented

Delivered:

- interactive project setup
- `minimal`, `standard`, and `strict` presets
- richer template context for Python version and tooling choices
- interactive tooling selection on top of preset defaults
- optional generated GitHub Actions CI workflow
- optional git initialization

## Phase 3: Post-Generation Expansion

Status: implemented

Delivered:

- `add http <function-name>`
- `add timer <function-name>`
- `add queue <function-name>`
- `add blob <function-name>`
- `add servicebus <function-name>`
- automatic `function_app.py` registration updates

## Phase 4: Template Expansion

Status: implemented for simple local-first triggers

Delivered:

- timer-focused project template
- queue-focused project template
- blob-focused project template
- service bus-focused project template
- generated-project smoke coverage across all simple trigger templates

Planned:

- richer project structure variants

## Phase 5: CLI Expansion

Status: implemented

Delivered:

- dry-run mode for `new` and `add` commands
- overwrite protections with `--overwrite` flag
- finer interactive tooling selection beyond presets

## Phase 6: Product Expansion

Status: implemented

Delivered:

- `--with-openapi` / `--no-openapi` flag for OpenAPI documentation (HTTP template)
- `--with-validation` / `--no-validation` flag for request validation (HTTP template)
- `--with-doctor` / `--no-doctor` flag for `azure-functions-doctor` health checks
- `azure-functions-logging` integration across all templates (structured JSON logging)
- Conditional `make doctor` target in generated projects
- Non-HTTP function templates use `logging.info()` instead of `print()`
## Out of Scope for Near Term

- telemetry frameworks
- tracing abstractions
- runtime middleware ecosystems
- large Azure SDK opinion bundles

