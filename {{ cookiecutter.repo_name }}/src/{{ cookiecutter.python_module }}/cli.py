"""Console script for {{cookiecutter.project_name}}"""
import logging
import os
import pathlib

import click
from nbis import decorators
from nbis.cli import setup_commands

from . import __version__
from . import commands


__author__ = "Per Unneberg"

logger = logging.getLogger(__name__)


@click.group(help=__doc__)
@click.version_option(version=__version__)
@decorators.debug_option()
@click.pass_context
def cli(ctx):
    """Cli help"""
    ctx.ensure_object(dict)
    logging.basicConfig(
        level=logging.INFO, format="%(levelname)s [%(name)s:%(funcName)s]: %(message)s"
    )
    if ctx.obj["DEBUG"]:
        logging.getLogger().setLevel(logging.DEBUG)
    try:
        from {{cookiecutter.project_name}} import config

        ctx.obj["ROOT"] = config.ROOT_DIR
    except ImportError:
        ctx.obj["ROOT"] = pathlib.Path(os.curdir)


def main():
    setup_commands(commands, cli)
    cli(obj={})
