# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_address = input ('Введите ip адрес в формате address:')
ip_address = ip_address.split('.')
ip_is_correct = True

""" проверка коррекстности ввода """

if len(ip_address) == 4:
    for ip in ip_address:
        if ip.isdigit():
            pass
        else:
            ip_is_correct = False
            break
        if int(ip) >= 0 and int(ip) <= 255:
            pass
        else:
            ip_is_correct = False
            break
else:
    ip_is_correct = False
      
""" тело скрипта по усуловию коррекстности ввода адреса """
        
if ip_is_correct:
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
else:
    print('Неправильный IP-адрес')
