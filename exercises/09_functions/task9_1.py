# -*- coding: utf-8 -*-

""" 
Сделать копию функции generate_access_config из задания 9.1.

Дополнить скрипт: ввести дополнительный параметр, который контролирует 
будет ли настроен port-security:

имя параметра «psecurity»

по умолчанию значение None

для настройки port-security, как значение надо передать список команд 
port-security (находятся в списке port_security_template)

Функция должна возвращать список всех портов в режиме access с 
конфигурацией на основе шаблона access_mode_template и шаблона 
port_security_template, если он был передан. В конце строк в списке не 
должно быть символа перевода строки.

Проверить работу функции на примере словаря access_config, с генерацией 
конфигурации port-security и без.

Пример вызова функции:

print(generate_access_config(access_config, access_mode_template))
print(generate_access_config(access_config, access_mode_template, port_security_template))
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security"
]

access_config = {
    "FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17
}

access_config_2 = {
    "FastEthernet0/03": 100,
    "FastEthernet0/07": 101,
    "FastEthernet0/09": 107,
}

def generate_access_config(intf_vlan_mapping, access_template, port_sec = []):
	"""
	intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого 
	вида:
		{"FastEthernet0/12": 10,
		"FastEthernet0/14": 11,
		"FastEthernet0/16": 17}
	access_template - список команд для порта в режиме access
	
	Возвращает список всех портов в режиме access с конфигурацией на 
	основе шаблона
	"""
	
	tmp_list = []
	command_tmpl = access_template + port_sec
	
	for intf, vlan in intf_vlan_mapping.items():
		tmp_list.append("interface " + intf)
		for command in command_tmpl:
			if command.endswith("access vlan"):
				tmp_list.append(command + " " +str(vlan))
			else:
				tmp_list.append(command)
	return(tmp_list)
		

def main():
	print(generate_access_config(access_config_2, access_mode_template, port_security_template))

if __name__ == "__main__":
    main()
    
