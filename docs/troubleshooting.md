# Troubleshooting Guide

This guide provides solutions for common issues encountered while using Azure Functions Scaffold. Most user facing errors are raised as a ScaffoldError with a descriptive message.

## Installation Issues

Problem: Command not found after installation
Cause: The CLI entry point is not in your system PATH.
Solution: Check the pip install location and ensure your Python scripts directory is in your PATH. As a fallback, use `python -m azure_functions_scaffold.cli`. Alternatively, install the package using pipx to handle path management automatically.

Problem: Python version incompatible
Cause: Azure Functions Scaffold requires Python 3.10 or higher.
Solution: Verify your current version with `python --version`. If it is below 3.10, install a newer version from python.org or your system package manager.

## Project Creation Issues

Problem: "Invalid project name" error
Cause: Project names must start with an alphanumeric character and only contain letters, numbers, hyphens, or underscores.
Solution: Use a valid name format.
Valid examples: `my-function-app`, `Project_01`, `azure-functions`.
Invalid examples: `-my-app`, `project!`, `123 app`.

Problem: Destination directory already exists
Cause: A directory with the chosen project name already exists in the target location.
Solution: Either choose a different name or destination, or use the --overwrite flag to replace the existing directory.

Problem: "Unknown template" error
Cause: The specified template type is not supported or does not exist.
Solution: Run `azure-functions-scaffold templates` to see the list of available options. Supported templates include:
- http
- timer
- queue
- blob
- servicebus

Problem: "Unknown preset" error
Cause: The specified preset level does not exist.
Solution: Run `azure-functions-scaffold presets` to see available options. Supported presets are:
- minimal
- standard
- strict

Problem: "Unsupported Python version" error
Cause: The specified target Python version is not in the supported list.
Solution: Ensure you are targeting one of the supported versions: 3.10, 3.11, 3.12, 3.13, or 3.14.

## Feature Flag Issues

Problem: --with-openapi has no effect with non-HTTP template
Cause: OpenAPI support is specifically designed for and only applicable to HTTP triggers.
Solution: Use the `--template http` option when enabling OpenAPI with `--with-openapi`.

Problem: --with-validation has no effect with non-HTTP template
Cause: Request validation support is only applicable to HTTP triggers.
Solution: Use the `--template http` option when enabling validation with `--with-validation`.

## Function Addition Issues

Problem: "Project root not found" or missing function_app.py
Cause: The --project-root argument does not point to a valid directory scaffolded by this tool.
Solution: Ensure the target directory contains a `function_app.py` file created during the initial project scaffolding.

Problem: Unsupported trigger type
Cause: The requested trigger type is not supported by the tool.
Solution: Use one of the supported triggers: http, timer, queue, blob, or servicebus.

## Generated Project Issues

Problem: Generated project fails `pytest`
Cause: Missing development dependencies or an incorrect Python version specified in the generated `pyproject.toml`.
Solution: Navigate into the generated project directory and run `pip install -e .[dev]` to install all necessary testing tools.

Problem: Generated project fails `ruff check`
Cause: This might indicate a template rendering issue or an outdated version of the scaffold tool.
Solution: If a freshly generated project fails linting out of the box, please report it as a bug.

Problem: Azure Functions Core Tools errors
Cause: The `func` CLI is not installed, outdated, or misconfigured.
Solution: Install the Azure Functions Core Tools. Note that this is a separate Microsoft tool and is not bundled with Azure Functions Scaffold.

## Interactive Mode Issues

Problem: Interactive prompts are confusing
Cause: First-time users might be unfamiliar with the various configuration options.
Solution: Safe and sensible defaults are provided for every prompt. You can safely press Enter to accept the default value for any option.

## Development Issues

Problem: make install fails
Cause: Python 3.10+ or pip is not available in the current environment.
Solution: Ensure that a compatible version of Python and pip are installed and accessible in your shell.

Problem: Pre-commit hooks fail
Cause: The code changes do not meet the formatting, linting, or type checking requirements.
Solution: Run `make format` to fix formatting issues automatically, followed by `make check-all` to identify and fix any remaining linting or type errors.

## General Error Handling

All user-facing errors are handled through the `ScaffoldError` exception. If you encounter an error not covered here, it will likely provide a specific message explaining what went wrong and how to fix it.

If you believe you have found a bug in the scaffolding process, please provide:
1. The command you ran
2. The full error message
3. Your Python version
4. Your operating system

This information helps in diagnosing and fixing template or CLI issues quickly.

The goal of this tool is to provide a clean, production-ready starting point. Keeping your local installation updated ensures you have the latest templates and bug fixes.

## Additional Resources

If you are still experiencing issues, consider the following steps:
1. Re-install the package to ensure you have the latest version.
2. Check your shell configuration for any conflicting aliases.
3. Review the official Azure Functions documentation for trigger-specific configurations.
4. Verify that your local Python environment is correctly activated.
5. Search through previous issues in the project's repository.

Taking these steps often resolves the most common environmental problems that can affect CLI tools.

## Reporting Bugs

When reporting an issue, being as detailed as possible will speed up the resolution process. Include the exact command that triggered the error, and if possible, a copy of the output from your terminal.

If the error occurs during the generation of a specific template, let us know which template and preset you were using at the time. This context is crucial for reproducing the issue and finding a fix.

---
EOF
