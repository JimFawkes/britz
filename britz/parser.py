# Copyright: (c) 2021, Moritz Eilfort
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from pglast import split, parse_sql, Node, prettify
from loguru import logger

from .objects import File, Table
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

    def get_tables(self):
        # TODO: Currently evaluating cte's as tables

        destination_table = False
        latest_destination = None

        for node in self.root_node[0].traverse():
            logger.debug(f"node={node}")
            node_tag = getattr(node, "node_tag", None)

            if node_tag in ("CreateTableAsStmt", "IntoClause"):
                destination_table = True

            if node_tag in ("query", "SelectStmt"):
                destination_table = False

            if getattr(node, "node_tag", None) == "RangeVar":
                persistent = node.relpersistence.value == "p"
                table = Table(
                    name=node.relname.value,
                    schema=getattr(node.schemaname, "value", ""),
                    persistent=persistent,
                    is_destination=destination_table,
                )

                if destination_table:
                    latest_destination = table
                elif not latest_destination is None:
                    latest_destination.source_tables[table.full_name] = table

                self.file.tables[table.full_name] = table

    def parse(self):
        for idx, query in enumerate(self.queries):
            logger.debug(f"Parsing query idx={idx}, query=\n{prettify(query)}\n")
            self.query = query
            self.root_node = Node(parse_sql(query))
            logger.debug(f"root_node={self.root_node}")
            self.get_tables()

        self.file.query_count = idx
        self.file.is_parsed = True
