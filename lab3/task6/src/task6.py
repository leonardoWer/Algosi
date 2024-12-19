"""
Сортировка целых чисел
"""

from lab3 import utils
from lab3.task1.src.task1 import quick_sort
import os


CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def get_data_c(lst_a:list, lst_b:list) -> list:
    """ Возвращает список, полученный перемножением одинаковых по индексу элементов списков"""
    return [i*j for i in lst_a for j in lst_b]


def sort_z_numbers(lst:list) -> int:
    """
    Сортирует список с помощью быстрой сортировки
     - Принимает: (список)
     - Возвращает (число - сумма каждого 10 элемента в отсортированном списке)
     """
    quick_sort(lst, 0, len(lst)-1)
    return sum([lst[i] for i in range(0, len(lst), 10)])


def input_data() -> (int, int, list, list):
    data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    n, m = map(int, data[0].split())
    lst_a = utils.str_to_list(data[1])
    lst_b = utils.str_to_list(data[2])
    return n, m, lst_a, lst_b


def main():
    n, m, lst_a, lst_b = input_data()
    lst_c = get_data_c(lst_a, lst_b)
    res = sort_z_numbers(lst_c)
    return res


if __name__ == "__main__":
    result = main()
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, [result])
