# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.
O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0
"""


output = """
            Prefix                {}
            AD/Metric             {}
            Next-Hop              {}
            Last update           {}
            Outbound Interface    {} """
        


with open('ospf.txt') as f:
    for line in f:
        line = line.replace('[',' ').replace(']',' ').replace(',','').split()
        print(output.format(line[1],line[2],line[4],line[5],line[6]))
            
             
    
