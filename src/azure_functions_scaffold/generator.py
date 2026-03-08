from __future__ import annotations

from pathlib import Path
import re

from azure_functions_scaffold.errors import ScaffoldError

FUNCTION_IMPORT_MARKER = "# azure-functions-scaffold: function imports"
FUNCTION_REGISTRATION_MARKER = "# azure-functions-scaffold: function registrations"
SUPPORTED_TRIGGERS = ("http", "timer")


def add_function(
    *,
    project_root: Path,
    trigger: str,
    function_name: str,
) -> Path:
    normalized_trigger = _normalize_trigger(trigger)
    normalized_name = _normalize_function_name(function_name)

    _validate_project_root(project_root)

    function_path = project_root / "app" / "functions" / f"{normalized_name}.py"
    if function_path.exists():
        raise ScaffoldError(f"Function module already exists: {function_path}")

    function_path.parent.mkdir(parents=True, exist_ok=True)
    function_path.write_text(
        _render_function_module(normalized_trigger, normalized_name),
        encoding="utf-8",
    )

    if (project_root / "tests").is_dir():
        test_path = project_root / "tests" / f"test_{normalized_name}.py"
        if not test_path.exists():
            test_path.write_text(
                _render_function_test(normalized_trigger, normalized_name),
                encoding="utf-8",
            )

    _update_function_app(
        project_root / "function_app.py",
        import_stmt=f"from app.functions.{normalized_name} import {normalized_name}_blueprint",
        registration_stmt=f"app.register_functions({normalized_name}_blueprint)",
    )

    return function_path


def _normalize_trigger(trigger: str) -> str:
    normalized = trigger.strip().lower()
    if normalized not in SUPPORTED_TRIGGERS:
        supported = ", ".join(SUPPORTED_TRIGGERS)
        raise ScaffoldError(f"Unsupported trigger '{trigger}'. Supported triggers: {supported}")
    return normalized


def _normalize_function_name(function_name: str) -> str:
    normalized = function_name.strip()
    if not normalized:
        raise ScaffoldError("Function name must not be empty.")

    module_name = re.sub(r"[^a-zA-Z0-9]+", "_", normalized).strip("_").lower()
    if not module_name:
        raise ScaffoldError("Function name must contain letters or numbers.")

    if module_name[0].isdigit():
        raise ScaffoldError("Function name must not start with a digit.")

    return module_name


def _validate_project_root(project_root: Path) -> None:
    if not project_root.exists():
        raise ScaffoldError(f"Project root does not exist: {project_root}")

    if not project_root.is_dir():
        raise ScaffoldError(f"Project root must be a directory: {project_root}")

    required_paths = [
        project_root / "function_app.py",
        project_root / "app" / "functions",
    ]
    missing = [path for path in required_paths if not path.exists()]
    if missing:
        raise ScaffoldError("Project root does not look like a scaffolded Azure Functions project.")


def _update_function_app(
    function_app_path: Path,
    *,
    import_stmt: str,
    registration_stmt: str,
) -> None:
    content = function_app_path.read_text(encoding="utf-8")

    if import_stmt in content or registration_stmt in content:
        raise ScaffoldError("Function is already registered in function_app.py.")

    updated = _insert_near_marker(
        content,
        marker=FUNCTION_IMPORT_MARKER,
        line=import_stmt,
        fallback_anchor="configure_logging()",
    )
    updated = _insert_near_marker(
        updated,
        marker=FUNCTION_REGISTRATION_MARKER,
        line=registration_stmt,
        fallback_anchor="app = func.FunctionApp()",
        after_anchor=True,
    )
    function_app_path.write_text(updated, encoding="utf-8")


def _insert_near_marker(
    content: str,
    *,
    marker: str,
    line: str,
    fallback_anchor: str,
    after_anchor: bool = False,
) -> str:
    if marker in content:
        return content.replace(marker, f"{line}\n{marker}", 1)

    if fallback_anchor not in content:
        raise ScaffoldError(
            f"Could not update function_app.py because '{fallback_anchor}' was not found."
        )

    if after_anchor:
        return content.replace(fallback_anchor, f"{fallback_anchor}\n{line}", 1)

    return content.replace(fallback_anchor, f"{line}\n\n{fallback_anchor}", 1)


def _render_function_module(trigger: str, function_name: str) -> str:
    route_name = function_name.replace("_", "-")

    if trigger == "http":
        return f"""from __future__ import annotations

import azure.functions as func

{function_name}_blueprint = func.Blueprint()


@{function_name}_blueprint.route(
    route="{route_name}",
    methods=["GET"],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def {function_name}(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        body="TODO: implement {route_name}",
        status_code=200,
    )
"""

    return f"""from __future__ import annotations

import logging

import azure.functions as func

{function_name}_blueprint = func.Blueprint()


@{function_name}_blueprint.timer_trigger(
    arg_name="timer",
    schedule="0 */5 * * * *",
    run_on_startup=False,
    use_monitor=True,
)
def {function_name}(timer: func.TimerRequest) -> None:
    if timer.past_due:
        logging.warning("Timer trigger '{function_name}' is running late.")

    logging.info("Timer trigger '{function_name}' executed.")
"""


def _render_function_test(trigger: str, function_name: str) -> str:
    if trigger == "http":
        route_name = function_name.replace("_", "-")
        return f"""from __future__ import annotations

import azure.functions as func

from app.functions.{function_name} import {function_name}


def test_{function_name}_returns_placeholder_response() -> None:
    request = func.HttpRequest(
        method="GET",
        url="http://localhost/api/{route_name}",
        params={{}},
        body=b"",
    )

    response = {function_name}(request)

    assert response.status_code == 200
    assert response.get_body() == b"TODO: implement {route_name}"
"""

    return f"""from __future__ import annotations

from types import SimpleNamespace

from app.functions.{function_name} import {function_name}


def test_{function_name}_runs_without_error() -> None:
    timer = SimpleNamespace(past_due=False)

    {function_name}(timer)
"""
