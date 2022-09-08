# -*- coding: utf-8 -*-

"""
Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить команды, в которых 
содержатся слова, которые указаны в списке ignore.
При этом скрипт также не должен выводить строки, которые начинаются на !.
Проверить работу скрипта на конфигурационном файле config_sw1.txt. 
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

ignore = ["duplex", "alias", "configuration"]
"""


import os
from sys import argv

# для Windous указываем дирикторию
os.chdir(r"C:\Users\vasils\Documents\python\pyneng\lesson_7")


ignore = ["duplex", "alias", "configuration"]
input_file = argv[1]

with open(input_file) as f:
	for line in f:
		words = line.split()
		words_intersect = set(words)&set(ignore)
		if not line[0].startswith("!") and not words_intersect:
			print(line, end=' ')
