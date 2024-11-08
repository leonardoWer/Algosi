"""
Анти-быстрая сортировка
"""

from lab3 import utils


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


if __name__ == "__main__":
    n = utils.read_file_1()
    res = anti_qsort(n)
    utils.write_file([res])
