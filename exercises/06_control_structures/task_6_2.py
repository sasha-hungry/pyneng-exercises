# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_address = input ('Введите ip адрес в формате address:')
ip_address = ip_address.split('.')
a=int(ip_address[0])
b=int(ip_address[1])
c=int(ip_address[2])
d=int(ip_address[3])

if a >= 1 and a <= 223 :
    print('unicast')
elif a >= 224 and a <=239 :
    print('multicast')
elif a == 255 and b == 255 and c == 255 and d == 255 :
    print ('local broadcast')
elif a==0 and b == 0 and c == 0 and d == 0 :
    print ('unassigned')
else:
    print('unused')
