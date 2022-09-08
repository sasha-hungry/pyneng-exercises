# -*- coding: utf-8 -*-

"""
Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

while True:
	ip_address = input("Введите IP-адрес в формате 10.0.1.1 :")
	octets = ip_address.split(".")
	correct_ip_flag = True
	if len(octets) != 4:
		correct_ip_flag = False
	else:
		for octet in octets:
			if not (octet.isdigit() and int(octet) in range(0,256)):
				correct_ip_flag = False
				break
	if correct_ip_flag == False:
		print("неправильный IP аддрес")
	else:
		break

	
octet1 = int(octets[0])	
if ip_address == "255.255.255.255":
	print("local broadcast")
elif ip_address == "0.0.0.0":
	print("unassigned")
elif octet1 >= 1 and octet1 <= 223:
	print("unicast")
elif octet1 >= 224 and octet1 <= 239:
	print("multicats")
else:
	print("unused")
