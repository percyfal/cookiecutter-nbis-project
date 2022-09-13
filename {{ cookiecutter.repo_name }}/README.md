<!--
[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.repo_name }})
-->
<!--
[![CI](https://github.com/NBISweden/{{ cookiecutter.project_name }}/actions/workflows/ci.yml/badge.svg)](https://github.com/NBISweden/{{ cookiecutter.project_name }}/actions/workflows/ci.yml)
-->
<!--
[![BioConda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg)](http://bioconda.github.io/recipes/{{ cookiecutter.repo_name }}/README.html)
-->

`FIXME`: add information about your project in this file

# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

# Installation

This repo was initialized with the cookiecutter
[cookiecutter-nbis-project](https://github.com/percyfal/cookiecutter-nbis-project).
The repo has to be under source control, whereafter it can be
installed:

	git init
	git add -f .
	pip install -e .
	
This will install the python module `{{ cookiecutter.project_name }}`
which can be invoked as

	{{ cookiecutter.project_name }}
	

## Project organization

```
{{ cookiecutter.project_name }}/                         <- top-level project folder
| 
├── README.md
├── pyproject.toml
├── setup.cfg
└── src                                                  <- source code
    └── {{ cookiecutter.project_name }}                  <- python module code
        └── commands                                     <- python module commands
```
