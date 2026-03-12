# Testing Guide

## Overview

The azure-functions-scaffold project uses pytest as its primary test framework. The test suite includes three main files containing approximately 1,166 lines of test code. These tests ensure the reliability of CLI commands, project scaffolding logic, and function generation.

## Running Tests

Execute tests using the provided Makefile or directly via hatch.

### Run All Tests
```bash
make test
```

### Run with Coverage
This command generates terminal reports showing missing lines, along with HTML and XML reports for deeper analysis.
```bash
make cov
```

### Run Specific Test File
Use hatch to run a single test file with verbose output for debugging.
```bash
hatch run pytest tests/test_cli.py -v
```

## Test Structure

| File | Lines | Description |
| :--- | :--- | :--- |
| `test_cli.py` | 558 | CLI command tests using Typer's CliRunner |
| `test_scaffolder.py` | 437 | Project generation and template rendering |
| `test_generator.py` | 171 | Function addition to existing projects |

## Test Patterns

### CLI Tests (test_cli.py)
These tests focus on the user interface and command execution logic.
- Uses `typer.testing.CliRunner` to invoke commands directly.
- Verifies command output, exit codes, and error messages.
- Simulates user input to test interactive mode.
- Validates the dry-run flag for both `new` and `add` commands.
- Checks flag behavior for --with-openapi, --with-validation, and --with-doctor.
- Confirms correct output for template and preset listing commands.

### Scaffolder Tests (test_scaffolder.py)
Scaffolder tests ensure that the core project creation logic works correctly across different environments.
- Leverages the `tmp_path` fixture for isolated file system testing.
- Tests project generation for all supported trigger types, including http, timer, queue, blob, and servicebus.
- Validates project naming rules, checking for valid names, invalid characters, and empty strings.
- Tests preset resolution for minimal, standard, and strict configurations.
- Verifies template rendering across various flag and option combinations.
- Ensures overwrite behavior functions as expected without accidental data loss.
- Checks the integrity of the generated project structure and file contents.

### Generator Tests (test_generator.py)
These tests ensure that adding new functions to an existing project remains consistent.
- Validates adding functions to previously scaffolded project directories.
- Tests all supported trigger types within the generator context.
- Confirms function name validation logic.
- Tests error handling when attempting to add functions to non-existent project roots.

## Coverage Configuration

The project's coverage settings are defined in `pyproject.toml`:
- Source directory: `src/azure_functions_scaffold`.
- Branch coverage: Enabled to ensure all logical paths are tested.
- Exclusions: Template `.j2` files are omitted from raw coverage reports because they are verified through integration tests in the scaffolder.
- Reporting: Includes terminal summaries (with missing lines), HTML reports, and XML output for CI integration.

## Writing New Tests

Follow these guidelines when expanding the test suite:

1. Place CLI-related tests in `test_cli.py` following the `CliRunner` pattern.
2. Place scaffolding logic tests in `test_scaffolder.py` using the `tmp_path` fixture for isolation.
3. Place function addition tests in `test_generator.py`.
4. Use descriptive naming conventions: `test_<feature>_<scenario>`.
5. Always implement tests for both success paths and error conditions.
6. When introducing new template features, test all possible flag combinations to prevent regressions.

### Example Test Pattern

```python
from typer.testing import CliRunner
from azure_functions_scaffold.cli import app

runner = CliRunner()

def test_new_project_with_http_template(tmp_path):
    # Setup the destination path
    project_name = "my-api"
    
    # Invoke the CLI command
    result = runner.invoke(app, ["new", project_name, "--destination", str(tmp_path)])
    
    # Assertions
    assert result.exit_code == 0
    assert (tmp_path / project_name / "function_app.py").exists()
```

## CI Test Matrix

The project maintains high compatibility standards through an automated CI pipeline defined in `.github/workflows/ci-test.yml`.
- Operating System: `ubuntu-latest`.
- Python Versions: 3.10, 3.11, 3.12, 3.13, 3.14.

## Troubleshooting Test Failures

### tmp_path Cleanup
Pytest handles the cleanup of `tmp_path` directories automatically. If you need to inspect the files after a failure, use the `--basetemp` flag with pytest to specify a persistent location.

### Template Rendering Errors
If tests fail during rendering, verify the Jinja2 syntax within the `templates/` directory. Small syntax errors in templates often manifest as broad execution failures.

### Import Errors
Ensure that all development dependencies are correctly installed. Run `make install` to refresh the environment and install pytest, pytest-cov, and coverage.
