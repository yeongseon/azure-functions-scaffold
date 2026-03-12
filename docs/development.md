# Development Guide

This guide provides information for contributors on how to set up the development environment, understand the project structure, and use the provided tools to maintain code quality.

## Prerequisites

To contribute to this project, ensure you have the following installed on your system:

- Python 3.10 or higher
- Git
- GNU Make

## Setting Up the Development Environment

The project uses Hatch for environment management and a Makefile as the primary entry point for development tasks. Follow these steps to prepare your local environment:

```bash
git clone https://github.com/yeongseon/azure-functions-scaffold.git
cd azure-functions-scaffold
make install
```

The `make install` command performs several actions:
1. Creates a local virtual environment.
2. Installs Hatch.
3. Initializes the Hatch environment with all dependencies.
4. Installs pre-commit hooks to ensure code quality before every commit.

## Project Layout

The codebase is organized into several key components within the `src/azure_functions_scaffold/` directory:

```text
src/azure_functions_scaffold/
|- __init__.py          # Package version definition
|- cli.py               # Typer CLI application entry point
|- scaffolder.py         # Core logic for project generation
|- generator.py          # Logic for adding functions to projects
|- template_registry.py  # Registry for templates and presets
|- models.py             # Frozen dataclasses for data structures
|- errors.py             # Custom ScaffoldError exception
|- templates/            # Jinja2 project and function templates
|  |- http/              # HTTP trigger templates
|  |- timer/             # Timer trigger templates
|  |- queue/             # Queue trigger templates
|  |- blob/              # Blob trigger templates
|  `- servicebus/        # Service Bus trigger templates
tests/
|- test_cli.py           # Tests for CLI commands
|- test_scaffolder.py    # Tests for project generation
`- test_generator.py     # Tests for function addition
docs/                    # Source files for MkDocs documentation
```

## Makefile Targets

Use these Make commands to manage your development workflow:

| Target | Description |
|--------|-------------|
| `make install` | Initial environment setup |
| `make format` | Format code using ruff and black |
| `make lint` | Run style checks and static type analysis |
| `make test` | Execute the full test suite |
| `make cov` | Run tests and generate coverage reports |
| `make security` | Perform security scanning with bandit |
| `make check-all` | Run the full quality gate (lint, test, security) |
| `make docs` | Build the documentation using MkDocs |
| `make docs-serve` | Serve documentation locally with hot reloading |
| `make build` | Create distribution packages (wheel and sdist) |
| `make clean` | Remove standard build artifacts |
| `make clean-all` | Perform a deep clean of all caches and environments |

## Code Quality Tools

The project enforces strict quality standards through several integrated tools. These are executed automatically by pre-commit hooks or manually via Make targets.

- black (26.3.0): Enforces a consistent code style with a line length of 100 characters.
- ruff (v0.15.5): Handles linting and import sorting with a line length of 100 characters.
- mypy (v1.19.1): Performs static type checking in strict mode.
- bandit (1.9.4): Scans the source directory for potential security vulnerabilities.
- pre-commit: Orchestrates the execution of all tools mentioned above.

## Running Tests

Testing is handled via pytest within the Hatch environment. You can run tests using the Makefile or directly through Hatch.

```bash
make test                          # Execute all tests
make cov                           # Run tests with a coverage report
hatch run pytest tests/test_cli.py # Run a specific test file
```

The coverage report includes terminal output, HTML reports, and XML files for CI integration.

## Working with Templates

Templates are the core of the scaffolding engine. They are located in `src/azure_functions_scaffold/templates/` and organized by trigger type.

- Templates use Jinja2 syntax and carry the `.j2` extension.
- Available context variables include `project_name`, `project_slug`, `python_version`, `include_openapi`, `include_validation`, and `include_doctor`.
- When modifying templates, you must verify the output by ensuring a generated project passes its own tests, lints correctly, and adheres to formatting rules.

## Version Management

The package version is centrally defined in `src/azure_functions_scaffold/__init__.py`. Versioning follows semantic versioning principles.

To release a new version, use the following commands:
- `make release-patch` for bug fixes.
- `make release-minor` for new features.
- `make release-major` for breaking changes.

Changelog updates are automatically generated from conventional commit messages using git-cliff during the release process.

## Building and Publishing

Once your changes are tested and verified, you can build and publish the package using the following commands:

```bash
make build            # Generate wheel and sdist files
make publish-test     # Upload the package to TestPyPI
make publish-pypi     # Upload the package to the official PyPI
```

Ensure you have the necessary credentials configured for the target repositories before attempting to publish.
