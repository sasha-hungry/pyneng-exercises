#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

from sys import argv

input_filename = argv[1]
output_filename = argv[2]

with open(input_filename) as src, open(output_filename, 'w') as dest:
    for line in src:
        command = line.split()
        ingnore_include = set(command)&set(ignore) # списоки конвертируются во множеста и находится их пересечение
        if not line.startswith('!') and not ingnore_include:  # если строка не начиниается с ! и пересечние списка ignored со словами из строки то print (наличе какого либо значения для python есть true)
            dest.write(line)
