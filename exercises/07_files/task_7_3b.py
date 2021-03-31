# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
result=[]
input_vlan = input('Enter VLAN number:')

with open('CAM_table.txt') as f:
    for line in f:
        line_list=line.split()
        if line_list and line_list[0].isdigit() :
            result.append([int(line_list[0]),line_list[1],line_list[3]]) #добавляем прямо список, номер vlan записываем как число

for vlan,mac,interface in result:
    if int(input_vlan) == vlan :
        print('{:<9} {:20} {}'.format(vlan,mac,interface))
