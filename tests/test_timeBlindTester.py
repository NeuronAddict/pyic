import random
import time
from unittest import TestCase

from pyic.time_blind_tester import TimeBlindTester


class MockResponse:
    def __init__(self, text=''):
        self.text = text
        self.status_code = 200
        self.headers = {}


def rb(payload):
    random.seed()
    if payload == '1=0':
        t = random.uniform(0, 3)
        time.sleep(t / 100)

    if payload == '1=1':
        t = random.uniform(7, 10)
        time.sleep(t / 100)
    return MockResponse()


def bad_rb(payload):
    random.seed()
    if payload == '1=0':
        t = random.uniform(0, 1)
        time.sleep(t / 100)

    if payload == '1=1':
        t = random.uniform(1, 0)
        time.sleep(t / 100)
    return MockResponse()


def bad_rb2(payload):
    random.seed()
    if payload == '1=0':
        time.sleep(0.1)

    if payload == '1=1':
        time.sleep(0.1)
    return MockResponse()


class TestTimeBlindTester(TestCase):

    def test_test(self):
        tbt = TimeBlindTester(rb)
        for i in range(0, 9):
            self.assertEqual(tbt.test('1=0'), False)
            self.assertEqual(tbt.test('1=1'), True)

    def test_bad_callibrate(self):
        def f():
            TimeBlindTester(bad_rb)

        self.assertRaises(Exception, f)

        def f2():
            TimeBlindTester(bad_rb2)

        self.assertRaises(Exception, f2)
