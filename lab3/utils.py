"""
В файле собраны функции-удобства:
 - Чтение файла input.txt
 - Запись в файл output.txt
"""

import datetime
import tracemalloc

import_path = "../txtfiles/"

# Функции для работы с файлами

def read_file() -> (int, list):
    """
    Функция считывает данные с файла
     - В файле построчно должны быть: (число, список)
     - Возвращает: (число, список)
    """
    path = import_path + "input.txt"
    file_in = open(path)
    variable_1 = int(file_in.readline())
    variable_2 = list(map(int, file_in.readline().split()))
    file_in.close()

    return variable_1, variable_2


def write_file(data: list):
    """
    Функция записывает данные в файл
     - Принимает на вход список всех данных, которые нужно записать
     - Записывает данные в файл
    """
    path = import_path + "output.txt"
    file_out = open(path, "w")
    for el in data:
        if type(el) == list:
            res = " ".join([str(i) for i in el])  # Список с результатом приводим к строке и записываем в файл
            file_out.write(res)
            if len(data) > 1 and data[-1] == el and type(data[-1]) == list:
                file_out.write("\n")
        elif type(el) == int:
            file_out.write(str(el))
        elif type(el) == str:
            file_out.write(el)
        if len(data) > 1 and data[-1] != el:
            file_out.write("\n")
    file_out.close()


def read_file_4() -> (int, list, int, list):
    """
    Функция считывает данные с файла
     - В файле построчно должны быть: (число, список, число список)
     - Возвращает: (число, список, число, список)
    """
    path = import_path + "input.txt"
    file_in = open(path)
    variable_1 = int(file_in.readline())
    variable_2 = list(map(int, file_in.readline().split()))
    variable_3 = int(file_in.readline())
    variable_4 = list(map(int, file_in.readline().split()))
    file_in.close()

    return variable_1, variable_2, variable_3, variable_4


def read_file_1() -> int:
    """
    Функция считывает данные с файла
     - В файле построчно должны быть: число
     - Возвращает: число
    """
    path = import_path + "input.txt"
    file_in = open(path)
    variable_1 = int(file_in.readline())
    file_in.close()

    return variable_1


def read_file_1_list() -> list:
    """
    Функция считывает данные с файла
     - В файле построчно должны быть: список
     - Возвращает: список
    """
    path = import_path + "input.txt"
    file_in = open(path)
    variable_1 = list(map(int, file_in.readline().split()))
    file_in.close()

    return variable_1


# Функции для тестов времени и памяти для разных функций

def test_memory_and_time_lst(lst: list, func, need_print:bool):
    """
    Выводит затрачиваемое время и память для сортировки
    - Формат входных данных вызова: (список, функция, нужно ли выводить результат)
    - Формат входных данных для функции (список)
    - Результат функции не выводит
    """
    print(f"Просчитаем время и память работы Сортировки {func}")
    tracemalloc.start()  # Запускаем счётчик памяти
    start_time = datetime.datetime.now()  # Запускаем счётчик времени

    func(lst)
    if need_print:
        if func(lst) is not None:
            print(func(lst))
        else:
            print(lst)

    finish_time = datetime.datetime.now()  # Измеряем время конца работы
    print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

    current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
    print(
        f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах


def test_memory_and_time_lst_n(lst: list, n: int, func, need_print:bool):
    """
    Выводит затрачиваемое время и память для сортировки
    - Формат входных данных вызова: (список, количество элементов, функция, нужно ли выводить результат)
    - Формат входных данных для функции (список, левый, правый)
    - Результат функции не выводит
    """
    print(f"Просчитаем время и память работы Сортировки {func}")
    tracemalloc.start()  # Запускаем счётчик памяти
    start_time = datetime.datetime.now()  # Запускаем счётчик времени

    func(lst, 0, n - 1)
    if need_print:
        if func(lst, 0, n - 1) is not None:
            print(func(lst, 0, n - 1))
        else:
            print(lst)

    finish_time = datetime.datetime.now()  # Измеряем время конца работы
    print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

    current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
    print(
        f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах
