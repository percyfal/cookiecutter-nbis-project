import sys


# Needs package installation -> run in tox only
def test_cli(project, capsys):
    """Test that cli includes subcommands from nbis_project_admin and project"""
    sys.path.insert(0, str(project.parent))
    sys.path.insert(0, str(project))
    import project_name.cli as cli

    try:
        cli.main(["-h"])
    except SystemExit:
        pass
    out, err = capsys.readouterr()
    assert "example" in out
    assert "webexport" in out
