"""
Быстрая сортировка +
"""

from random import *
import os
from lab3 import utils


CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def quick_sort(lst: list, left: int, right: int):
    """
    Функция быстрой сортировки
    """
    if left < right:
        m = partition(lst, left, right)
        quick_sort(lst, left, m - 1)
        quick_sort(lst, m + 1, right)


def partition(lst: list, left: int, right: int) -> int:
    """
    Функция, которая отвечает за разделение
     - возвращает индекс последнего элемента, для которого было сделано перемещение
    """
    x = lst[left]  # Выбираем "опорный" элемент
    j = left
    for i in range(left + 1, right + 1):
        if lst[i] <= x:
            j += 1
            lst[j], lst[i] = lst[i], lst[j]
    lst[left], lst[j] = lst[j], lst[left]
    return j


def randomized_quick_sort(lst: list, left: int, right: int):
    """
    Функция быстрой сортировки, которая использует рандомные элементы
    """
    if left < right:
        k = randint(left, right)
        lst[left], lst[k] = lst[k], lst[left]
        m = partition(lst, left, right)
        randomized_quick_sort(lst, left, m - 1)
        randomized_quick_sort(lst, m + 1, right)


def input_data():
    data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    n, lst = int(data[0]), utils.str_to_list(data[1])
    n1, lst1 = int(data[0]), utils.str_to_list(data[1])
    return n, lst, n1, lst1


def main():
    n, lst, n1, lst1 = input_data()
    quick_sort(lst, 0, n - 1)
    randomized_quick_sort(lst1, 0, n1 - 1)
    result = [lst, lst1]
    return result


if __name__ == "__main__":
    result = main()
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, result)
