"""
Copyright: (c) 2020, Moritz Eilfort
GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
This module tests all helper methods
"""

import pytest

from . import helpers
from .helpers import get_parse_args

from britz.cli import parser


def test_mock_args_is_in_sync_with_argparse():
    mock_args = helpers.MockArgs()
    cli_args = parser.parse_args(args=[])

    assert vars(mock_args) == vars(cli_args)
