from unittest import TestCase

from pyic.body_conditions import HasText, Not


class MockRequest:
    def __init__(self, text):
        self.text = text


class TestBodyConditions(TestCase):
    def test_HasText(self):
        self.assertEqual(True, HasText('text').__call__(MockRequest('*text and other')))
        self.assertEqual(False, HasText('text').__call__(MockRequest('ext bla bla')))

        self.assertEqual(False, Not(HasText('text')).__call__(MockRequest('*text and other')))
        self.assertEqual(True, Not(HasText('text')).__call__(MockRequest('ext bla bla')))
