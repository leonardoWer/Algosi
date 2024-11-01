"""
Быстрая сортировка + с выделением 3-го списка из равных элементов
"""

from random import *
from lab3 import utils


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


if __name__ == "__main__":
    n, lst = utils.read_file()  # Количество элементов и список с элементами
    randomized_quick_sort_three(lst, 0, n - 1)

    res = [1,2,2,2,1,1,14,5,67,7,5,7,4342,2,34,234,23,423,4,553456,1,1,1,43,324,23,5,23452,1]
    randomized_quick_sort_three(res,0, len(res)-1)

    utils.write_file([lst, res])
