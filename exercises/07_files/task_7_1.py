# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

f = open('c:\\Users\\steep\\Documents\\dotnetlessons\\gitlessons\\my_pyneng_tasks\\exercises\\07_files\\ospf.txt')

output_template = '''
Prefix                {0}
AD/Metric             {1}
Next-Hop              {2}
Last update           {3}
Outbound Interface    {4}
'''

output_file = f.readlines()
for lines_file in output_file:
    # count = 0
    lines_file = lines_file.replace(',', '')
    lines_file = lines_file.replace('[', '')
    lines_file = lines_file.replace(']', '')
    lines_file = lines_file.removesuffix('\n')
    lines_file = lines_file.replace('O', '')
    lines_file = lines_file.strip()
    lines_file = lines_file.split(' ')
    # count += 1
    print(output_template.format(lines_file[0], lines_file[1], lines_file[3], lines_file[4], lines_file[5]))

# print(format('',output_file))

# print(f'Prefix\t{f.readline().split(' ') }')
