"""
Help for example subcommand.

This is an example help string.

Copy/rename file to a module that runs a subcommand. The module file
must contain at least an add_arguments function.

"""


def add_arguments(parser):
    arg = parser.add_argument
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--dry-run", "-n", action="store_true", default=False, help="dry run"
    )

    arg("--json", metavar="FILE", help="json output", default="example.json")


def main(args):
    print("Default runner")
