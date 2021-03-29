# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


ip_is_correct = False

# проверка коррекстности ввода

while not ip_is_correct:
    ip_address = input ('Введите ip адрес:')
    ip_address = ip_address.split('.')
    if len(ip_address) == 4:
        for ip in ip_address:
            if ip.isdigit() and int(ip) in range(256):
                ip_is_correct = True
            else:
                print('Неправильный IP-адрес')
                ip_is_correct = False
                break
    else:
        print('Неправильный IP-адрес')
                
    
     
# тело скрипта по усуловию коррекстности ввода адреса 
        
a=int(ip_address[0])
b=int(ip_address[1])
c=int(ip_address[2])
d=int(ip_address[3])

if a in range(1,224):
    print('unicast')
elif a in range (224,240):
    print('multicast')
elif a == 255 and b == 255 and c == 255 and d == 255 :
    print ('local broadcast')
elif a==0 and b == 0 and c == 0 and d == 0 :
    print ('unassigned')
else:
    print('unused')

