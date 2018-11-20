from unittest import TestCase

from pysqli.body_conditions import HasText, Not


class TestBodyConditions(TestCase):
    def test_HasText(self):
        self.assertEqual(True, HasText('text').__call__('*text and other'))
        self.assertEqual(False, HasText('text').__call__('ext bla bla'))

        self.assertEqual(False, Not(HasText('text')).__call__('*text and other'))
        self.assertEqual(True, Not(HasText('text')).__call__('ext bla bla'))

