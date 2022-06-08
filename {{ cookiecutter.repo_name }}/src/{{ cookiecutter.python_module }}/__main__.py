import logging
import sys
from argparse import ArgumentDefaultsHelpFormatter
from argparse import ArgumentParser

from . import __version__

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


def __cc_main__(arguments=None):
    if arguments is None:
        arguments = sys.argv[1:]

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")  # noqa
    logging.info("Running main")

    parser = DescriptionArgumentParser(description=__doc__, prog="nbis")
    parser.add_argument(
        "--version", action="version", version="%(prog)s " + __version__
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        default=False,
        help="Print debug messages",
    )


try:
    from nbis.__main__ import main as __nbis_main__

    main = __nbis_main__
except Exception as e:
    logger.debug(e)
    logger.debug("using __cc_main__")
    main = __cc_main__
