# Contributing Guide

This guide provides information for developers looking to contribute to the azure-functions-scaffold project. This project follows high standards for code quality, testing, and documentation to ensure the generated scaffolds are reliable for production use.

## Project Scope

Contributions should improve one of these areas:
- CLI usability and interactive experience
- Template quality and generated project structure
- Test coverage and security scanning
- Documentation and guides


This guide provides information for developers looking to contribute to the azure-functions-scaffold project. This project follows high standards for code quality, testing, and documentation to ensure the generated scaffolds are reliable for production use.

## Getting Started

To begin contributing, follow these steps to set up your local development environment:

1. Fork the repository on GitHub.
2. Clone your fork to your local machine.
3. Run the following command to install dependencies and set up the development environment:

```bash
make install
```

4. Verify your setup by running the full check suite:

```bash
make check-all
```

## Development Workflow

We follow a standard feature branch workflow:

1. Create a new feature branch from the main branch.
2. Implement your changes in the `src/azure_functions_scaffold/` directory.
3. If you are adding new functionality or fixing a bug, add corresponding tests in the `tests/` directory.
4. Run `make check-all` locally to ensure all linting, typing, and tests pass.
5. Commit your changes using the Conventional Commits specification.
6. Push your branch to your fork and create a pull request against the main repository.

## Commit Message Convention

This project uses Conventional Commits to automate versioning and changelog generation via git-cliff.

| Type | Description |
|------|-------------|
| feat | A new feature |
| fix | A bug fix |
| docs | Documentation only changes |
| style | Changes that do not affect the meaning of the code (white-space, formatting, etc) |
| refactor | A code change that neither fixes a bug nor adds a feature |
| test | Adding missing tests or correcting existing tests |
| chore | Changes to the build process or auxiliary tools and libraries |

Example commit messages:
- `feat: add support for blob trigger templates`
- `fix: resolve incorrect path handling in windows environments`
- `docs: update contributing guide with testing requirements`

## Code Quality Standards

We enforce strict code quality standards through pre-commit hooks and CI checks:

- **black (26.3.0)**: Used for code formatting with a line length of 100.
- **ruff (v0.15.5)**: Used for linting and import sorting.
- **mypy (v1.19.1)**: Used for static type checking in strict mode.
- **bandit (1.9.4)**: Used for security scanning to identify common security issues.
- **forbid-korean**: A custom pre-commit hook ensuring all documentation and source code are in English.

You must maintain a minimum of 90 percent test coverage for all pull requests.

## Testing Requirements

Comprehensive testing is required for all contributions:

- Add tests for any changes to CLI behavior or template rendering.
- Use `CliRunner` from the `typer` library for testing CLI commands.
- Use the `tmp_path` fixture for scaffolder tests to ensure isolated file system operations.
- Ensure you test both successful execution and expected error cases.

## Template Change Guidelines

Modifying templates under `src/azure_functions_scaffold/templates/` requires additional verification because these templates generate code for end users:

1. Verify that the project generated from your modified template can run its own tests using `pytest`.
2. Verify that the generated project passes its own `ruff check .` linting.
3. Verify that the generated project passes its own `ruff format --check .` formatting check.
4. Ensure the generated code preserves compatibility with the Azure Functions Python v2 programming model.
5. Template output must be deterministic. Avoid any logic that produces different results for the same input parameters.
6. The generated code must remain clean, well-commented, and easy for users to edit by hand.

## Pull Request Process

- Ensure all CI checks pass, including linting, typing, and tests.
- Keep your changes aligned with the project goals defined in `PRD.md` and `DESIGN.md`.
- Prefer small, focused pull requests that are easy to review.
- Update the documentation in the `docs/` directory if your changes affect user-facing behavior.

## Version Management

The project version is maintained in `src/azure_functions_scaffold/__init__.py`. We follow Semantic Versioning (SemVer):

- **Major version**: For breaking changes.
- **Minor version**: For new features that are backwards compatible.
- **Patch version**: For backwards compatible bug fixes.

The `CHANGELOG.md` file is automatically updated via git-cliff during the release process based on commit messages.

## Code of Conduct

All contributors are expected to be respectful and inclusive. Please refer to the `CODE_OF_CONDUCT.md` file in the repository root for more detailed information.
