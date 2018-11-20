def encode_str(sql_str):
    return '0x' + sql_str.encode('ascii').hex()

def es(sql_str):
    return encode_str(sql_str)

class SqliEncoder:
    
    def str_to_hexa(sql_str):
        return '0x' + sql_str.encode('ascii').hex()

    def str_to_char(sql_str):
        """ Encode the string with the CHAR technique.

        'MySQL' become CHAR(77,121,83,81,'76').
        see https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_char
        """
        ret = 'CHAR('
        i = 1
        for c in sql_str:
            ret += str(ord(c))
            if i != len(sql_str):
                ret += ','
            i += 1
        return ret + ')'


