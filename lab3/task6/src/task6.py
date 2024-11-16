"""
Сортировка целых чисел
"""

from lab3 import utils
from lab3.task1.src.task1 import quick_sort


def get_data_c(lst_a:list, lst_b:list) -> list:
    """ Возвращает список, полученный перемножением одинаковых по индексу элементов списков"""
    return [i*j for i in lst_a for j in lst_b]


def read_input_file_2_numbers_2_lists() -> (int, int, list, list):
    """ Считывает с файла два числа и два списка """
    file_in = open("../txtfiles/input.txt")
    n, m = map(int, file_in.readline().split())
    lst_a = list(map(int, file_in.readline().split()))
    lst_b = list(map(int, file_in.readline().split()))
    file_in.close()
    return n, m, lst_a, lst_b


def sort_z_numbers(lst:list) -> int:
    """
    Сортирует список с помощью быстрой сортировки
     - Принимает: (список)
     - Возвращает (число - сумма каждого 10 элемента в отсортированном списке)
     """
    quick_sort(lst, 0, len(lst)-1)
    return sum([lst[i] for i in range(0, len(lst), 10)])


if __name__ == "__main__":
    n, m, lst_a, lst_b = read_input_file_2_numbers_2_lists()
    lst_c = get_data_c(lst_a, lst_b)
    res = sort_z_numbers(lst_c)

    utils.write_file([res])
