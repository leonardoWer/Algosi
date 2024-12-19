"""
Анти-быстрая сортировка
"""

import os
from lab3 import utils


CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def qsort(lst: list, left: int, right: int):
    """ Алгоритм быстрой сортировки"""
    key = lst[(left + right) // 2]
    i = left
    j = right
    while i <= j:
        while lst[i] < key:
            i += 1
        while lst[j] > key:
            j -= 1
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
    if left < j:
        qsort(lst, left, j)
    if i < right:
        qsort(lst, i, right)


def anti_qsort(n: int) -> list:
    """ Возвращает худшую перестановку от длинны списка"""
    res = list(range(1, n + 1))

    for i in range(2, n):
        swap(res, i // 2, i)

    return res


def swap(lst: list, i: int, j: int):
    """ Меняет элементы списка местами """
    lst[i], lst[j] = lst[j], lst[i]


def input_data():
    data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    n = int(data[0])
    return n


def main():
    n = input_data()
    result = anti_qsort(n)
    return result


if __name__ == "__main__":
    result = main()
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, [result])
