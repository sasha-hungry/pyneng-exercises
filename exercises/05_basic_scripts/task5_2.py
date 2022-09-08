"""
Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:

In [1]: "1" * 28 + "0" * 4
Out[1]: "11111111111111111111111111110000"
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""



prefix = input("Введите ip address в формате 10.1.1.0/24 :")
ip_address, mask = prefix.split("/")
mask = int(mask)

oct1, oct2, oct3, oct4 = ip_address.split(".")

ip_oct1 = int(oct1)
ip_oct2 = int(oct2)
ip_oct3 = int(oct3)
ip_oct4 = int(oct4)

bin_mask = "1" * mask + "0" * (32 - mask)

mask_oct1 = int(bin_mask[0:8],2)
mask_oct2 = int(bin_mask[8:16],2)
mask_oct3 = int(bin_mask[16:24],2)
mask_oct4 = int(bin_mask[24:],2)


net_template = """
Network:

{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
"""

mask_template = """
Mask:
/{0}
{1:<10}{2:<10}{3:<10}{4:<10}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
"""

print(net_template.format(ip_oct1,ip_oct2,ip_oct3,ip_oct4))
print(mask_template.format(mask, mask_oct1, mask_oct2, mask_oct3, mask_oct4))

