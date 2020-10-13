"""
Copyright: (c) 2020, Moritz Eilfort
GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""

import pytest
from unittest.mock import patch

from britz import cli, __version__

from . import helpers
from .helpers import get_parse_args


def test_argument_parser_exits_for_missing_required_args(get_parse_args):
    with pytest.raises(SystemExit) as e:
        args = get_parse_args()

    assert e.value.code != 0


def test_argument_parser_exits_for_version_arg(get_parse_args):
    with pytest.raises(SystemExit) as e:
        args = get_parse_args(["--version"])

    assert e.value.code == 0


def test_print_version(capsys):

    cli.print_version()

    captured = capsys.readouterr()
    cleaned_output = captured.out.replace("\n", "")

    assert __version__ in cleaned_output


def test_britz_cli_with_only_filename():

    args = helpers.MockArgs(filename="some/filename.sql")

    with pytest.raises(SystemExit) as e:
        cli.britz_cli(args)

    assert e.value.code == 0


@patch("britz.cli.britz_cli")
@patch("britz.cli.parse_args")
def test_cli_function(mock_britz_cli, mock_parse_args):
    cli.cli(parser=lambda: None)

    assert mock_britz_cli.called
    assert mock_parse_args.called
