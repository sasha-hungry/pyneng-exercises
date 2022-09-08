# -*- coding: utf-8 -*-

"""
Сделать копию скрипта задания 6.2.
Добавить проверку введенного IP-адреса. Адрес считается корректно заданным,
если он: состоит из 4 чисел (а не букв или других символов)
числа разделенны точкой
каждое число в диапазоне от 0 до 255
Если адрес задан неправильно, выводить сообщение: «Неправильный IP-адрес».
Сообщение «Неправильный IP-адрес» должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

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

