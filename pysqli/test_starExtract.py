from unittest import TestCase

from pysqli.star_extract import StarExtract


class MockResponse:
    def __init__(self, text):
        self.text = text


class TestStarExtract(TestCase):

    def test_StartExtract(self):
        self.assertEqual('pattern', StarExtract('blah</h2><h2>*</h2>')
                         .__call__(MockResponse('<h2>blah</h2><h2>pattern</h2>blah')))

    def test_StartExtract_withshift(self):
        self.assertEqual('pattern', StarExtract('<h2>*</h2>', 8)
                         .__call__(MockResponse('<h2>blah</h2><h2>pattern</h2>blah')))
