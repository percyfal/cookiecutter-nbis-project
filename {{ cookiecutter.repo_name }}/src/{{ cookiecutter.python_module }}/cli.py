"""Console script for {{cookiecutter.project_name}}"""
import logging
import sys

from nbis import cli

from . import __version__
from . import subcommands

__author__ = "Per Unneberg"

logger = logging.getLogger(__name__)


def main(arg_list=None):
    if arg_list is None:
        arg_list = sys.argv[1:]
        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        from nbis import subcommands as nbis_subcommands

        package_list = [subcommands, nbis_subcommands]
    except ModuleNotFoundError:
        package_list = [subcommands]
    top_parser = cli.get_top_parser("{{ cookiecutter.python_module }}", __version__)
    minimal_parser, subcommands_map = cli.make_minimal_parser(top_parser, package_list)
    subcommand_name = cli.get_subcommand_name(minimal_parser, arg_list)
    top_parser = cli.get_top_parser("{{ cookiecutter.python_module }}", __version__)
    # fmt: off
    parser = cli.make_subcommand_parser(
        top_parser, subcommand_name, subcommands_map[subcommand_name]
    )
    # fmt: on

    args, extra = parser.parse_known_args(arg_list)

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    del args.debug

    args.project_name = "{{ cookiecutter.project_name }}"
    args.prog = parser.prog
    args.extra_options = extra
    args.runner(args)

    return 0
