# -*- coding: utf-8 -*-

"""
Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный 
файл коммутатора и возвращает кортеж из двух словарей:

словарь портов в режиме access, где ключи номера портов, 
а значения access VLAN (числа):

{"FastEthernet0/12": 10,
 "FastEthernet0/14": 11,
 "FastEthernet0/16": 17}
словарь портов в режиме trunk, где ключи номера портов, а значения 
список разрешенных VLAN (список чисел):

У функции должен быть один параметр config_filename, который ожидает 
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import os
import pathlib
from pathlib import Path

def get_int_vlan_map(config_filename):
    """
    Функция обрабатывает конфигурационный файл коммутатора Cisco и
    возвращает кортедж из двух словарей: словарь портов в режиме access,
    где ключи номера портов, а занчения номера vlan-ов(числа) и словарь 
    trunk - где ключи номера портов, а значения разрешенные vlan-s
    в виде спосока чисел.
    
    config_filename - имя конфигурационного файла.
    """
    access_dict = dict()
    trunk_dict =dict()
    
    with open(config_filename) as config_file:
        for line in config_file:
            line = line.rstrip()
            # находим интерфесы
            if line.startswith("interface"):
                intf = line.split()[-1]
            # проверяем на access
            elif "access vlan" in line:
                access_vlans = int(line.split()[-1])
                access_dict[intf] = access_vlans
            # проверяем на trunk    
            elif "trunk allowed vlan" in line:
                str_trunk_vlans = line.split()[-1].split(",")
                trunk_vlans = [int(vlan) for vlan in str_trunk_vlans]
                trunk_dict[intf] = trunk_vlans
    return(access_dict,trunk_dict,)
                

def main():
    """
    основное тело скрипта
    """
    # задаем рабочую директорию (важно для кросс платформенности)
    dir_path = pathlib.Path.cwd()
    current_directory = Path(dir_path)
    os.chdir(current_directory)
    
    print(get_int_vlan_map('config_sw1.txt'))

if __name__ == "__main__":
    main()
