import pytest

# Until there is a nbis_project_admin package, skip tests if package
# not installed

try:
    import nbis  # noqa: F401
except ModuleNotFoundError:
    pytest.skip(
        "skip nbis_admin tests due to missing nbis_project_admin package",
        allow_module_level=True,
    )
