# -*- coding: utf-8 -*-

"""
Создать функцию generate_trunk_config, которая генерирует конфигурацию
для trunk-портов.
У функции должны быть такие параметры:

intf_vlan_mapping: ожидает как аргумент словарь с соответствием 
интерфейс-VLANы такого вида:

{"FastEthernet0/1": [10, 20],
 "FastEthernet0/2": [11, 30],
 "FastEthernet0/4": [17]}

trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов 
в виде списка команд (список trunk_mode_template)

Функция должна возвращать список команд с конфигурацией на основе 
указанных портов и шаблона trunk_mode_template. В конце строк в списке 
не должно быть символа перевода строки.

Проверить работу функции на примере словаря trunk_config и списка команд
trunk_mode_template. Если эта проверка прошла успешно, проверить работу 
функции еще раз на словаре trunk_config_2 и убедится, что в итоговом списке 
правильные номера интерфейсов и вланов.

Пример итогового списка (перевод строки после каждого элемента сделан для 
удобства чтения):

[
"interface FastEthernet0/1",
"switchport mode trunk",
"switchport trunk native vlan 999",
"switchport trunk allowed vlan 10,20,30",
"interface FastEthernet0/2",
"switchport mode trunk",
"switchport trunk native vlan 999",
"switchport trunk allowed vlan 11,30",
...]
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    """
    генерирует конфигурацию для trunk портов Cisco.
    intf_vlan_mapping - словарь (dict), где ключ имя интерфеса, а значение 
    список vlan's
    trunk_template - список (list) комманд в виде строк.
    """
    tmp_intf_cfg = []
    for intf, vlans in intf_vlan_mapping.items():
        tmp_intf_cfg.append("interface " + intf)
        for command in trunk_template:
            if command.endswith("allowed vlan"):
                str_vlans = ",".join([str(vlan) for vlan in vlans])
                tmp_intf_cfg.append(command + str_vlans)
            else:
                tmp_intf_cfg.append(command)
    return(tmp_intf_cfg)

def main():

    trunk_mode_template = [
    "switchport mode trunk", "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
    ]
    
    trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]
    }
   
    print(generate_trunk_config(trunk_config, trunk_mode_template))

if __name__ == "__main__":
    main()
