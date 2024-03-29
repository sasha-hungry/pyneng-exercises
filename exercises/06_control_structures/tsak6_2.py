# -*- coding: utf-8 -*-

"""
Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
«unicast» - если первый байт в диапазоне 1-223
«multicast» - если первый байт в диапазоне 224-239
«local broadcast» - если IP-адрес равен 255.255.255.255
«unassigned» - если IP-адрес равен 0.0.0.0
«unused» - во всех остальных случаях
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_address = input("Введите IP-адрес в формате 10.0.1.1 :")

ip_address_list = ip_address.split(".")

octet1 = int(ip_address_list[0])
octet2 = int(ip_address_list[1])
octet3 = int(ip_address_list[2])
octet4 = int(ip_address_list[3])

if octet1 >= 1 and octet1 <= 223:
	print("unicast")
elif octet1 >= 224 and octet1 <= 239:
	print("multicats")
elif octet1 == octet2 and octet2 == octet3 and octet3 == octet4 and octet4 == 255:
	print("local broadcast")
elif octet1 == octet2 and octet2 == octet3 and octet3 == octet4 and octet4 == 0:
	print("unassigned")
else:
	print("unused")


print(octet1, octet2, octet3, octet4)
