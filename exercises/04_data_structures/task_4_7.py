# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

mac = "AAAA:BBBB:CCCC"

# делим mac на группы по : и каждую группу в совю переменную
mac_a=mac.split(':')[0]
mac_b=mac.split(':')[1]
mac_c=mac.split(':')[2]

# выполняем преобразование из hex в dec, а затем стразу в bin.
# каждый bin преобразуем в строку и берем данные начиная со 2-го числа (0b- отрезаем)
# складываем занчения для получения общйе строки

result=str(bin(int(mac_a,16)))[2:]+str(bin(int(mac_b,16)))[2:]+str(bin(int(mac_c,16)))[2:]

print(result)

