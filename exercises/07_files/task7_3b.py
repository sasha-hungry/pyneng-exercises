# -*- coding: utf-8 -*-

"""
Сделать копию скрипта задания 7.3a.

Переделать скрипт:
Запросить у пользователя ввод номера VLAN.
Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8
Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


import os

os.chdir(r"C:\Users\vasils\Documents\python\pyneng\lesson_7")

input_vlan_number = input("Enter VLAN number: ")


with open("CAM_table.txt") as f:
	for line in f:
		line = line.split()
		# проверка, что список line существует и что он не нулевой
		# и проверка, что 1-ый элемент содержит числа
		if line and line[0].isdigit() and line[0] == input_vlan_number:
			vlan, mac, _, intf = line
			print("{:<9}{:<20}{:<}".format(vlan,mac,intf))

	
