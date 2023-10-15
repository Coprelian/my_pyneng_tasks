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


ip = input('Введите ip: ')
len_ip = len(ip.split('.'))
if len_ip != 4:
   print('Неправильный IP-адрес')
else:
   ip_int = ip.split('.')
   for octet in ip_int:
      try:
         octet = int(octet)
         if not 0 <= octet <=255:
            print('Неправильный IP-адрес')
            break
      except ValueError:
         print('Неправильный IP-адрес')
         break
   else:
      first_octet = int(ip.split('.')[0])

      if 0 < first_octet <= 223:
         result = 'unicast'
      elif 223 < first_octet <= 239:
         result = 'multicast'
      elif ip == '255.255.255.255':
         result = 'local broadcast'
      elif ip == '0.0.0.0':
         result = 'unassigned'
      else: 
         result = 'unused'
      print(result)