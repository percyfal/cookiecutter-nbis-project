import pytest


def test_bake_project(cookies):
    result = cookies.bake(template=str(pytest.cookie_template))
    assert result.exit_code == 0
