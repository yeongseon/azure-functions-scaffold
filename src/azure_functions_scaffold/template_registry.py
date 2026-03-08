from __future__ import annotations

from pathlib import Path

from azure_functions_scaffold.errors import ScaffoldError
from azure_functions_scaffold.models import PresetSpec, ProjectOptions, TemplateSpec

TEMPLATE_ROOT = Path(__file__).parent / "templates"
SUPPORTED_PYTHON_VERSIONS = ("3.10", "3.11", "3.12", "3.13", "3.14")


def list_templates() -> list[TemplateSpec]:
    return [
        TemplateSpec(
            name="http",
            description="HTTP-trigger Azure Functions Python v2 application.",
            root=TEMPLATE_ROOT / "http",
        )
    ]


def get_template(name: str) -> TemplateSpec:
    normalized_name = name.strip().lower()
    for template in list_templates():
        if template.name == normalized_name:
            return template

    available = ", ".join(template.name for template in list_templates())
    raise ScaffoldError(f"Unknown template '{name}'. Available templates: {available}")


def list_presets() -> list[PresetSpec]:
    return [
        PresetSpec(
            name="minimal",
            description="Minimal HTTP function with no additional quality tooling.",
            tooling=(),
        ),
        PresetSpec(
            name="standard",
            description="HTTP function with Ruff and pytest defaults.",
            tooling=("ruff", "pytest"),
        ),
        PresetSpec(
            name="strict",
            description="HTTP function with Ruff, mypy, and pytest defaults.",
            tooling=("ruff", "mypy", "pytest"),
        ),
    ]


def get_preset(name: str) -> PresetSpec:
    normalized_name = name.strip().lower()
    for preset in list_presets():
        if preset.name == normalized_name:
            return preset

    available = ", ".join(preset.name for preset in list_presets())
    raise ScaffoldError(f"Unknown preset '{name}'. Available presets: {available}")


def build_project_options(
    *,
    preset_name: str,
    python_version: str,
    include_github_actions: bool,
    initialize_git: bool,
) -> ProjectOptions:
    preset = get_preset(preset_name)
    validate_python_version(python_version)
    return ProjectOptions(
        preset_name=preset.name,
        python_version=python_version,
        tooling=preset.tooling,
        include_github_actions=include_github_actions,
        initialize_git=initialize_git,
    )


def validate_python_version(python_version: str) -> str:
    normalized_version = python_version.strip()
    if normalized_version not in SUPPORTED_PYTHON_VERSIONS:
        available = ", ".join(SUPPORTED_PYTHON_VERSIONS)
        raise ScaffoldError(
            f"Unsupported Python version '{python_version}'. Supported versions: {available}"
        )
    return normalized_version
