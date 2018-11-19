def encode_str(str):
	return '0x' + str.encode('ascii').hex()

def es(str):
	return encode_str(str)

