import sys

import pytest
from click.testing import CliRunner


@pytest.fixture
def runner(request):
    return CliRunner()


# Needs package installation -> run in tox only
def test_cli(project, runner):
    """Test that cli includes commands from nbis_project_admin and project"""
    sys.path.insert(0, str(project.parent))
    sys.path.insert(0, str(project))
    from project_name import commands
    from project_name.cli import cli
    from nbis.cli import setup_commands

    setup_commands(commands, cli)

    results = runner.invoke(cli, [])
    assert "admin" in results.output

    results = runner.invoke(cli.commands["admin"], [])
    assert "webexport" in results.output
