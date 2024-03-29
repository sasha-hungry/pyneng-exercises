"""
Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети, 
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.
Пример адреса сети (все биты хостовой части равны нулю):

10.0.1.0/24
190.1.0.0/16
Пример адреса хоста:

10.0.1.1/24 - хост из сети 10.0.1.0/24
10.0.5.195/28 - хост из сети 10.0.5.192/28
Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
Проверить работу скрипта на разных комбинациях хост/маска, например: 10.0.5.195/28, 10.0.1.1/24

Подсказка:

Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит адреса хоста + 4 ноля. 
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет bin_ip = "00001010000000010000000111000011".
А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего в адресе может быть 32 бита, а 32 - 28 = 4): 00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

prefix = input("Введите ip address в формате 10.1.1.0/24 :")
ip_address, mask = prefix.split("/")
mask = int(mask)

oct1, oct2, oct3, oct4 = ip_address.split(".")

in_ip_oct1 = int(oct1)
in_ip_oct2 = int(oct2)
in_ip_oct3 = int(oct3)
in_ip_oct4 = int(oct4)

bin_ip = "{:08b}{:08b}{:08b}{:08b}".format(in_ip_oct1,in_ip_oct2,in_ip_oct3,in_ip_oct4)
bin_mask = "1" * mask + "0" * (32 - mask)

bin_net_address = bin_ip[:mask] + "0"*(32-mask)

ip_oct1 = int(bin_net_address[:8],2)
ip_oct2 = int(bin_net_address[8:16],2)
ip_oct3 = int(bin_net_address[16:24],2)
ip_oct4 = int(bin_net_address[24:],2)

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
