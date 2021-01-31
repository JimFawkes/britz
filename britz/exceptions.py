# Copyright: (c) 2021, Moritz Eilfort
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
Module bundling all custom exception types.
"""


class InputFileError(Exception):
    """An Error occured when reading the given input file."""
