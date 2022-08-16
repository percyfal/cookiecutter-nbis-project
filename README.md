[![CI](https://github.com/percyfal/cookiecutter-nbis-project/actions/workflows/ci.yml/badge.svg)](https://github.com/percyfal/cookiecutter-nbis-project/actions/workflows/ci.yml)

# cookiecutter-nbis-project

A cookiecutter template for [NBIS](https://nbis.se/) projects.

# Features

This cookiecutter installs a bare minimum directory structure for
[NBIS](https://nbis.se/) projects. Project administration is deployed
to helper module
[nbis-project-admin](https://github.com/percyfal/nbis-project-admin).
`nbis-admin` provides a set of commands for use in project management.

# Usage

	cookiecutter https://github.com/percyfal/cookiecutter-nbis-project
	cd [project_name]
	git init
	git add -f .
	pip install -e .
	project_name -h


Following installation, python modules added to the directory
`src/project_name/subcommands` will automatically show up as a
subcommand when issuing the command `project_name`.


# Requirements

- [nbis-project-admin](https://github.com/percyfal/nbis-project-admin)

