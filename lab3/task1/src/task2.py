"""
Быстрая сортировка + с выделением 3-го списка из равных элементов
"""

from random import *
import os
from lab3 import utils


CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def randomized_quick_sort_three(lst: list, left: int, right: int):
    """
    Функция быстрой сортировки, которая использует рандомные элементы
    """
    if left < right:
        k = randint(left, right)
        lst[left], lst[k] = lst[k], lst[left]
        m = partition_three(lst, left, right)
        randomized_quick_sort_three(lst, left, m - 1)
        randomized_quick_sort_three(lst, m + 1, right)


def partition_three(lst: list, left: int, right: int):
    """
    Функция, которая отвечает за разделение
     - возвращает индекс последнего элемента, для которого было сделано перемещение
    """
    x = lst[left]  # Выбираем "опорный" элемент
    j = left
    i = left - 1
    p = right

    while j<=p:
        if lst[j] < x:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
            j += 1
        elif lst[j] > x:
            lst[j], lst[p] = lst[p], lst[j]
            p -= 1
        else:
            j += 1

    return p


def input_data():
    data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    n, lst = int(data[0]), utils.str_to_list(data[1])
    return n, lst


def main():
    n, lst = input_data()
    randomized_quick_sort_three(lst, 0, n - 1)
    result = [lst]
    return result


if __name__ == "__main__":
    result = main()
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, result)
