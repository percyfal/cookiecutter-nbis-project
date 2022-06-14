import pytest

# Failsafe in case nbis is not available in local test environment
try:
    import nbis  # noqa: F401
except ModuleNotFoundError:
    pytest.skip(
        "skip nbis_admin tests due to missing nbis_project_admin package",
        allow_module_level=True,
    )
