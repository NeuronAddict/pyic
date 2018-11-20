import unittest
from unittest import TestCase
from tools import *


class TestEncode_str(TestCase):

    def test_encode_hexa_legacy(self):
        self.assertEqual('0x41', encode_str('A'))
        self.assertEqual('0x2f6574632f706173737764', encode_str('/etc/passwd'))

    def test_encode_hexa(self):
        self.assertEqual('0x41', SqliEncoder.str_to_hexa('A'))
        self.assertEqual('0x2f6574632f706173737764', SqliEncoder.str_to_hexa('/etc/passwd'))

    def test_encode_char(self):
        self.assertEqual('CHAR(77,121,83,81,76)', SqliEncoder.str_to_char('MySQL'))
    

if __name__ == '__main__':
    unittest.main()
