# Copyright: (c) 2021, Moritz Eilfort
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
Module bundling all file read and write helper methods.
"""

from pathlib import Path

from .exceptions import InputFileError


def read_file(filename):
    """Read content of file."""

    with open(filename) as fd:
        content = fd.read()

    return content


def get_file_list(path, suffix=".sql"):
    """Construct list of files for given path and suffix."""

    sql_dir = Path(path)
    return sorted([str(filepath) for filepath in sql_dir.rglob(f"*{suffix}")])


def get_content(path, suffix=".sql"):
    """
    Get a generator iterating over the list of files constructed from the given
    path and suffix.


    TODO
    ----
    - Allow list of paths
    - Allow partial filenames e.g., `some/dir/some_file` resolving [some/dir/some_file_1.sql, some/dir/some_file_2.sql]

    """
    if Path(path).is_dir():
        files = get_file_list(path, suffix=suffix)
    elif Path(path).is_file():
        files = [path]
    else:
        raise InputFileError(f"Encountered UNKNOWN Object Type for path='{path}'")

    return (read_file(file) for file in files)
