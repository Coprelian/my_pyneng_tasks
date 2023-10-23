# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

output = ''
with open('c:\\Users\\steep\\Documents\\dotnetlessons\\gitlessons\\my_pyneng_tasks\\exercises\\07_files\\config_sw1.txt', 'r') as f:
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
                line = ' '.join(line)            
                output += line
print(output)