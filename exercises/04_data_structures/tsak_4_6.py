"""
Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

input_list = ospf_route.replace(",","").replace("[","").replace("]","").split()

output_template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""

print(output_template.format(input_list[0],
                             input_list[1],
                             input_list[3],
                             input_list[4],
                             input_list[5]))
