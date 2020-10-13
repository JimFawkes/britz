# Copyright: (c) 2020, Moritz Eilfort
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

help_text = """
britz

Easily review the dependencies between your SQL Transformations.
"""

import argparse
import logging
import sys

from britz import __version__, __author__, __url__, __license__, __copyright__

epilog = f"""
Version {__version__} - October 2020 - {__author__} - src: {__url__}
License {__license__} - {__copyright__}
"""


logger = logging.getLogger("britz.cli")

parser = argparse.ArgumentParser(
    prog="britz",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=help_text,
    epilog=epilog,
)


parser.add_argument("--version", "-v", help="Show current version", action="store_true")
parser.add_argument("--debug", "-d", help="Print Debug Messages", action="store_true")
parser.add_argument("--filename", "-f", help="SQL file to parse", type=str)


def print_version():
    print(f"britz {__version__}")


def setup_logging():
    # Default Logger
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    logger.debug("Set loglevel to DEBUG")


def parse_args(args):
    if args.version:
        print_version()
        sys.exit(0)

    if args.debug:
        setup_logging()

    if not args.filename:
        parser.error("Missing required argument: '--filename'")

    return args


def britz_cli(args):
    print()
    print("----------------------")
    print("- Nothing to do yet! -")
    print("----------------------")
    print()

    sys.exit(0)


def cli(parser=parser.parse_args):
    args = parse_args(parser())
    britz_cli(args)
