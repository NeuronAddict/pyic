from unittest import TestCase
from tools import *


class TestEncode_str(TestCase):
    def test_encode_str(self):
        self.assertEqual('0x41', encode_str('A'))
        self.assertEqual('0x2f6574632f706173737764', encode_str('/etc/passwd'))
