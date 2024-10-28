"""
В файле собраны функции-удобства:
 - Чтение файла input.txt
 - Запись в файл output.txt
"""
import tracemalloc
import datetime


import_path = "../txtfiles/"


def read_file() -> (int, list):
    """
    Функция считывает данные с файла
     - В файле построчно должны быть: (чило, список)
     - Возвращает: (число, список)
    """
    path = import_path + "input.txt"
    file_in = open(path)
    variable_1 = int(file_in.readline())
    variable_2 = list(map(int, file_in.readline().split()))

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
        elif type(el) == int:
            file_out.write(str(el))
        elif type(el) == str:
            file_out.write(el)
        if len(data) > 1 and data[-1] != el:
            file_out.write("\n")


def read_file_4() -> (int, list, int, list):
    """
    Функция считывает данные с файла
     - В файле построчно должны быть: (чило, список, числоб список)
     - Возвращает: (число, список, число, список)
    """
    path = import_path + "input.txt"
    file_in = open(path)
    variable_1 = int(file_in.readline())
    variable_2 = list(map(int, file_in.readline().split()))
    variable_3 = int(file_in.readline())
    variable_4 = list(map(int, file_in.readline().split()))

    return variable_1, variable_2, variable_3, variable_4

def test_func_on_data_from_example(func, n:int, lst:list):
    # На данных из примера
    print("Просчитаем время и память работы сортировки")
    tracemalloc.start()  # Запускаем счётчик памяти
    start_time = datetime.datetime.now()  # Запускаем счётчик времени

    print(func(lst))

    finish_time = datetime.datetime.now()  # Измеряем время конца работы
    print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

    current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
    print(f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах