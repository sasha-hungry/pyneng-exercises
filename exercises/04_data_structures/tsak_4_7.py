"""
Преобразовать MAC-адрес в строке mac в двоичную строку такого вида: „101010101010101010111011101110111100110011001100“

Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
"""
mac = "AAAA:BBBB:CCCC"

input_mac_list = mac.split(":")
out_mac_str = str(bin(int(input_mac_list[0],16)).lstrip('0b') + bin(int(input_mac_list[1],16)).lstrip('0b') \
+ bin(int(input_mac_list[2],16)).lstrip('0b'))

print(out_mac_str)



более элегантное решение
"""
mac = "AAAA:BBBB:CCCC"

bin_mac = "{:b}".format(int(mac.replace(":", ""), 16))
print(bin_mac)

