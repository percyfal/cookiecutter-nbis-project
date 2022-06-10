"""Console script for {{cookiecutter.project_name}}"""
# FIXME: make cookiecutter-nbis-project dependent on nbis-project-admin
import ast
import importlib
import logging
import pkgutil
import sys
from argparse import ArgumentDefaultsHelpFormatter
from argparse import ArgumentParser

from . import __version__
from . import subcommands

__author__ = "Per Unneberg"

logger = logging.getLogger(__name__)


class RawDescriptionDefaultsHelpFormatter(ArgumentDefaultsHelpFormatter):
    """Help message formatter which retains any formatting in
    descriptions and adds default values."""

    def _fill_text(self, text, width, indent):

        return "".join(indent + line for line in text.splitlines(keepends=True))  # noqa


class DescriptionArgumentParser(ArgumentParser):
    """An ArgumentParser that prints correctly formatted description
    and epilog help strings"""

    def __init__(self, *args, **kwargs):
        if "formatter_class" not in kwargs:
            kwargs["formatter_class"] = RawDescriptionDefaultsHelpFormatter
        super().__init__(*args, **kwargs)

    def error(self, message):
        self.print_help(sys.stderr)
        args = {"prog": self.prog, "message": message}
        self.exit(2, "%(prog)s: error: %(message)s\n" % args)


def get_project_parser(arg_list=None):
    if arg_list is None:
        arg_list = sys.argv[1:]

    parser = DescriptionArgumentParser(description=__doc__, prog="{{ cookiecutter.project_name }}")  # noqa
    parser.add_argument(
        "--version", action="version", version="%(prog)s " + __version__
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        default=False,
        help="Print debug messages",
    )
    return parser, arg_list


def add_project_subcommand_parser(parser, arg_list=None):
    subcommand_name = get_subcommand_name(arg_list)
    module = importlib.import_module(
        "." + subcommand_name, subcommands.__name__
    )  # noqa
    subparsers = parser.add_subparsers()
    subparser = subparsers.add_parser(
        subcommand_name,
        help=module.__doc__.split("\n", maxsplit=1)[1],
        description=module.__doc__,
    )
    module.add_arguments(subparser)
    return parser


def main(arg_list=None):
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")  # noqa
    parser, arg_list = get_project_parser(arg_list)
    args = parser.parse_args(arg_list)

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    del args.debug

    try:
        from nbis.cli import add_subcommand_parser

        parser = add_subcommand_parser(parser, arg_list)
    except Exception as e:
        logger.debug(e)

    parser = add_project_subcommand_parser(parser, arg_list=None)

    args = parser.parse_args(arg_list)


def get_subcommand_name(arguments) -> str:
    """Parse arguments to find out which subcommand was requested.

    This sets up a minimal ArgumentParser with the correct help
    strings.

    Because help is obtained from a module’s docstring, but importing
    each module makes startup slow, the modules are only parsed with
    the ast module and not fully imported at this stage.

    Return:
        subcommand name

    """
    parser = DescriptionArgumentParser(description=__doc__, prog="{{ cookiecutter.project_name }}")  # noqa
    parser.add_argument("--version", action="version", version=__version__)
    subparsers = parser.add_subparsers()

    for module_name, docstring in subcommands_modules(subcommands):
        hstring = docstring.split("\n", maxsplit=2)[1].replace("%", "%%")
        subparser = subparsers.add_parser(
            module_name, help=hstring, description=docstring, add_help=False
        )
        subparser.set_defaults(module_name=module_name)
    args, _ = parser.parse_known_args(arguments)
    module_name = getattr(args, "module_name", None)
    if module_name is None:
        parser.error("Please provide the name of a subcommand to run")
    return module_name


def subcommands_modules(package):
    """
    Yield (module_name, docstring) tuples for all modules in the given package.
    """
    modules = pkgutil.iter_modules(package.__path__)
    for module in modules:
        spec = importlib.util.find_spec(package.__name__ + "." + module.name)
        with open(spec.origin) as f:
            mod_ast = ast.parse(f.read())
        docstring = ast.get_docstring(mod_ast, clean=False)
        yield module.name, docstring
