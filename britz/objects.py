# Copyright: (c) 2021, Moritz Eilfort
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from dataclasses import dataclass


@dataclass
class BaseClass:
    name: str


class File(BaseClass):
    query_count: int = 0
    is_parsed: bool = False
