# -*- coding: utf-8 -*-

"""
Сделать копию скрипта задания 7.3.

Переделать скрипт: Отсортировать вывод по номеру VLAN В результате 
должен получиться такой вывод:

10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Обратите внимание на vlan 1000 - он должен выводиться последним. 
Правильной сортировки можно добиться, если vlan будет числом, а не строкой.

Ограничение: Все задания надо выполнять используя только пройденные темы..

"""


import os

os.chdir(r"C:\Users\vasils\Documents\python\pyneng\lesson_7")

tmp_list =[]

with open("CAM_table.txt") as f:
	for line in f:
		line = line.split()
		# проверка, что список line существует и что он не нулевой
		# и проверка, что 1-ый элемент содержит числа
		if line and line[0].isdigit():
			vlan, mac, _, intf = line
			vlan = int(vlan)
			tmp_list.append([vlan,mac,intf])

for vlan, mac, intf in sorted(tmp_list):
	print("{:<9}{:<20}{:<}".format(vlan,mac,intf))
