from unittest import TestCase

from pysqli.blindtester import BlindTester


class MockRequest:

    def __init__(self, text):
        self.text = text
        self.url = 'http://example.com'


class MockBlindTester(BlindTester):

    def __init__(self, text):
        super(MockBlindTester, self).__init__( lambda payload : MockRequest(payload), lambda a: a.text == text, True)


class TestTester(TestCase):

    def test_Tester(self):
        tester = MockBlindTester('payload')
        self.assertEqual(True, tester.test('payload'))
