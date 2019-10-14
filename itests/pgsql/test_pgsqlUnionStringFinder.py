from unittest import TestCase

import requests

from pyic import UnionStringFinder, StarExtract


class TestPGSQLUnionStringFinder(TestCase):

    def setUp(self):
        self.union_string_finder = UnionStringFinder('AND 1=0 UNION ALL SELECT 1,$$2$$,{}',
                                                     lambda payload: requests.get('http://127.0.0.1:8182/comment.php',
                                                                                  params={'id': '1 {}'.format(payload),
                                                                                          'log': '1'}),
                                                     StarExtract('<h2>2</h2><p>*</p>'))

    def test_read_string(self):
        self.assertEqual(self.union_string_finder.read_string('{}'.format('$$coucou$$')),
                         'coucou')

