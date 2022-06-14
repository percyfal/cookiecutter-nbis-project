"""
Help for example subcommand.

This is an example help string.

Copy/rename file to a module that runs a subcommand. The module file
must contain at least an add_arguments function and a main function.

"""


def add_arguments(parser):
    parser.add_argument(
        "--dry-run", "-n", action="store_true", default=False, help="dry run"
    )


def main(args):
    print("Default runner")
