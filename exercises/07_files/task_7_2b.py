# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 config_sw1.txt имя исходного файла конфигурации
 task_7_2b.txt имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
fileInput = argv[1]
fileOutput = argv[2]

ignore = ["duplex", "alias", "configuration"]

# output = ''
with open(fileInput) as f, open(fileOutput, 'w') as fw:
    for line in f:
        if not line.startswith('!'):
            line = line.split(' ')
            wordIgnore_in_line = False
            for word in line:
                for word_ignore in ignore:
                    if word == word_ignore:
                        wordIgnore_in_line = True
                        break
                if wordIgnore_in_line == True:
                    break
            else:
                # line = ' '.join(line)            
                # output += line
                fw.write(' '.join(line))
# print(output)