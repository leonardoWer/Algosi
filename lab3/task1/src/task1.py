"""
Быстрая сортировка +
"""

from random import *

from lab3 import utils


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


if __name__ == "__main__":
    n, lst = utils.read_file()  # Количество элементов и список с элементами
    n1, lst1 = utils.read_file()  # Количество элементов и список с элементами
    quick_sort(lst, 0, n - 1)
    randomized_quick_sort(lst1, 0, n1 - 1)
    utils.write_file([lst, lst1])
