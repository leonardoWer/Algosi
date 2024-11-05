"""
Сортировка вставкой +, дополнительно выводит номер, на который был поставлен элемент при обработке
"""

from lab1 import utils


def insertion_sort(n: int, lst: list):
    indexes = "1 "
    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while (j >= 0) and (lst[j] > key):
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
        indexes += str(j + 1 + 1) + " "

    return indexes, lst


if __name__ == "__main__":
    n, lst = utils.read_file()
    indexes, res = insertion_sort(n, lst)
    utils.write_file([indexes, res])