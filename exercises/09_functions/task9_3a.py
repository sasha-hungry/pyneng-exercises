# -*- coding: utf-8 -*-

"""
Сделать копию функции get_int_vlan_map из задания 9.3.
Дополнить функцию: добавить поддержку конфигурации, когда настройка 
access-порта выглядит так:

interface FastEthernet0/20
 switchport mode access
 duplex auto
То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, 
что порт в VLAN 1

У функции должен быть один параметр config_filename, который ожидает 
как аргумент имя конфигурационного файла.
Проверить работу функции на примере файла config_sw2.txt

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
            # находим интерфесы и всем им присваиваем VLAN access = 1
            if line.startswith("interface") and "Vlan" not in line:
                intf = line.split()[-1]
                access_dict[intf] = 1
            # проверяем на access и заменяем на нужный номер
            elif "access vlan" in line:
                access_vlans = int(line.split()[-1])
                access_dict[intf] = access_vlans
            # проверяем на trunk, если нашли убираем интерфес из access   
            elif "trunk allowed vlan" in line:
                del access_dict[intf]
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
    
    print(get_int_vlan_map('config_sw2.txt'))

if __name__ == "__main__":
    main()
