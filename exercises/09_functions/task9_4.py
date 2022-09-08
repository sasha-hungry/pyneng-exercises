# -*- coding: utf-8 -*-

"""
Создать функцию convert_config_to_dict, которая обрабатывает 
конфигурационный файл коммутатора и возвращает словарь:
Все команды верхнего уровня (глобального режима конфигурации), 
будут ключами.
Если у команды верхнего уровня есть подкоманды, они должны быть в 
значении у соответствующего ключа, в виде списка (пробелы в начале 
строки надо удалить).
Если у команды верхнего уровня нет подкоманд, то значение будет пустым 
списком
У функции должен быть один параметр config_filename, который ожидает 
как аргумент имя конфигурационного файла.
При обработке конфигурационного файла, надо игнорировать строки, 
которые начинаются с «!», а также строки в которых содержатся слова из 
списка ignore. Для проверки надо ли игнорировать строку, использовать 
функцию ignore_command.

Проверить работу функции на примере файла config_sw1.txt

Часть словаря, который должна возвращать функция (полный вывод можно 
посмотреть в тесте test_task_9_4.py):

"""

import os
import pathlib
from pathlib import Path
from pprint import pprint


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status
        
def convert_config_to_dict(config_filename):
    """
    Функция преобразует конфигурацию Cisco в словарь, где ключи - это команды верхннего уровня, а значения - список подкоманд.
    Если у команды нет подкоманды, 
    """
    ignore = ["duplex", "alias", "Current configuration"]
    
    cfg = dict()
    with open(config_filename) as cfg_file:
        for line in cfg_file:
            line = line.rstrip()
            if not line.startswith("!")and \
            ignore_command(line, ignore) != True:
                if line[0].isalnum():
                    upper_command = line
                    cfg[upper_command] = []
                else:
                    cfg[upper_command].append(line.lstrip())
    return(cfg)
                

    
def main():
    """
    Основное тело скрипта
    """
    dir_path = pathlib.Path.cwd()
    current_directory = Path(dir_path)
    os.chdir(current_directory)
    
    print(convert_config_to_dict('config_sw1.txt'))
    
    
if __name__ == "__main__":
    main()
