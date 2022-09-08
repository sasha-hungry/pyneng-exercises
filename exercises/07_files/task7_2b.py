# -*- coding: utf-8 -*-

"""
Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток 
вывода, скрипт должен записать полученные строки в файл
Имена файлов нужно передавать как аргументы скрипту:

имя исходного файла конфигурации
имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке 
ignore и строки, которые начинаются на „!“.

Ограничение: Все задания надо выполнять используя только пройденные темы.

ignore = ["duplex", "alias", "configuration"]
"""


import os
from sys import argv

os.chdir(r"C:\Users\vasils\Documents\python\pyneng\lesson_7")


ignore = ["duplex", "alias", "configuration"]
input_file = argv[1]
output_file = argv[2]

output_list = []

with open(input_file) as f:
	for line in f:
		words = line.split()
		words_intersect = set(words)&set(ignore)
		if not line[0].startswith("!") and not words_intersect:
			output_list.append(line.rstrip())

output_line = '\n'.join(output_list)

with open(output_file,'w') as out_f:
	out_f.write(output_line)
	
