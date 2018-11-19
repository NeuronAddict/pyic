from unittest import TestCase

from tester import Tester


class MockRequest:

    def __init__(self, text):
        self.text = text
        self.url = 'http://example.com'


class MockTester(Tester):

    def __init__(self, text):
        super(MockTester, self).__init__(lambda a: a.text == text, True)

    def get_request(self, payload):
        return MockRequest('payload')


class TestTester(TestCase):

    def test_Tester(self):
        tester = MockTester('payload')
        self.assertEqual(True, tester.test('payload'))
