def encode_str(sql_str):
    return '0x' + sql_str.encode('ascii').hex()


def es(sql_str):
    return encode_str(sql_str)
