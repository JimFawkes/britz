# Copyright: (c) 2021, Moritz Eilfort
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from pglast import split, parse_sql

from .objects import File
from .io import get_content


def parse_sql_files(path, suffix=".sql"):
    files = []
    contents = get_content(path, suffix=suffix)
    for content, filename in contents:
        query_parser = QueryParser(content=content, filename=filename)
        query_parser.parse()
        files.append(query_parser.file)

    return files


class QueryParser:
    def __init__(self, content, filename, config={}):
        self.content = content
        self.filename = filename
        self.config = config
        self.queries = split(self.content, safety_belt=False)
        self.file = File(name=self.filename)

    def parse(self):
        for idx, query in enumerate(self.queries):
            pass

        self.file.query_count = idx
        self.file.is_parsed = True
