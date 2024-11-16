"""
Сортировка вставкой базовая
"""

from lab1 import utils


def insertion_sort(n: int, lst: list) -> list:
    """
    - Проходимся по элементам массива, выбирам ключ
    - Сравниваем элементы, исходя из чего подбираем предполагаемую позицию
    - Ставим элемент на выбранный для него индекс
    """
    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while (j >= 0) and (lst[j] > key):
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


if __name__ == "__main__":
    n, lst = utils.read_file()
    res = insertion_sort(n, lst)
    utils.write_file([res])
