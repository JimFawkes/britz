# Copyright: (c) 2021, Moritz Eilfort
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from dataclasses import dataclass, field, asdict
from loguru import logger
from typing import List, Dict

from .io import write_object_to_file


@dataclass
class BaseClass:
    def write(self, dirname="data", type_="json"):
        filename = (
            f"{dirname}/{self.__class__.__name__}_{self.filename_suffix}_object.{type_}".lower()
        )
        write_object_to_file(filename, self.asdict(), type_)

    def asdict(self):
        return {self.full_name: asdict(self)}

    @property
    def full_name(self):
        return self.name

    @property
    def filename_suffix(self):
        return self.full_name.replace("/", "_").replace(".", "_").lower()


@dataclass
class Table(BaseClass):
    name: str
    schema: str
    persistent: bool
    is_destination: bool = False
    source_tables: Dict[str, "Table"] = field(default_factory=dict)

    @property
    def full_name(self):
        if self.schema:
            return f"{self.schema}.{self.name}"
        else:
            return self.name


@dataclass
class File(BaseClass):
    name: str
    query_count: int = 0
    is_parsed: bool = False
    tables: Dict[str, Table] = field(default_factory=dict)
