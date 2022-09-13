"""Administration utilities.

Nbis project administration code. See
https://github.com/percyfal/nbis-project-admin for more information.

"""
import logging

import click
from nbis.commands import *  # noqa: F405, F403
from {{cookiecutter.project_name}}.cli import cli


__shortname__ = __name__.split(".")[-1]


logger = logging.getLogger(__name__)


@cli.group(help=__doc__, name=__shortname__)
@click.pass_context
def main(ctx):
    logger.info(__shortname__)


main.add_command(config.main)  # noqa: F405
main.add_command(diary.main)  # noqa: F405
main.add_command(docs.main)  # noqa: F405
main.add_command(smk.main)  # noqa: F405
main.add_command(webexport.main)  # noqa: F405
