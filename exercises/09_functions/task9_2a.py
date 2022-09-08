# -*- coding: utf-8 -*-

"""
Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, 
а словарь:

ключи: имена интерфейсов, вида «FastEthernet0/1»
значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона 
trunk_mode_template.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


def generate_trunk_config(intf_vlan_mapping, trunk_template):
    """
    генерирует конфигурацию для trunk портов Cisco в виде словаря, где 
    ключ это имя интерфеса вида «FastEthernet0/1», а значение - 
    список команд.
    
    intf_vlan_mapping - словарь (dict), где ключ имя интерфеса, 
    а значение список vlan's
    trunk_template - список (list) комманд в виде строк.
    """
    tmp_intf_cfg = dict()
    for intf, vlans in intf_vlan_mapping.items():
        intf_cfg = []
        for command in trunk_template:
            if command.endswith("allowed vlan"):
                # конвертация номеров vlan из чисел в строки
                str_vlans = ",".join([str(vlan) for vlan in vlans])
                intf_cfg.append(command + str_vlans)
            else:
                intf_cfg.append(command)
        tmp_intf_cfg[intf] = intf_cfg
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
