# -*- coding: utf-8 -*-

"""
Обработать строки из файла ospf.txt и вывести информацию по каждой 
строке в таком виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


# для Windous указываем дерикторию
import os
os.chdir(r"C:\Users\vasils\Documents\python\pyneng\lesson_7")

output_tmpl = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""

with open("ospf.txt") as f:
	for line in f:
		r = line.replace(",","").replace("[","").replace("]","")
		r = r.split()
		
		print(output_tmpl.format(r[1],r[2],r[4],r[5],r[6]))
