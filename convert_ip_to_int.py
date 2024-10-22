def convert_ip_to_int(ip):
    split = str.split(ip, '.')
    concat_as_binary = ""
    for segment in split:
        binary = format(int(segment), '08b')
        concat_as_binary = concat_as_binary + binary

    return int(concat_as_binary, 2)


print(convert_ip_to_int('69.171.230.68'))
