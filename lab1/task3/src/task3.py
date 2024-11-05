"""
Сортировка вставкой в невозрастающем(убывающем) порядке
"""

from lab1 import utils


def reverse_insertion_sort(n:int, lst:list) -> list:
    """ Сортировка вставкой в порядке убывания"""
    for i in range(1, n):
        key = lst[i]
        j = i-1
        while (j>=0) and (lst[j]<key): # Поменялся знак неравенства, теперь нам подходит случай, когда предыдущий элемент меньше чем ключ
            lst[j+1] = lst[j]
            j -=1
        lst[j+1] = key

    return lst


if __name__ == "__main__":
    n, lst = utils.read_file()
    res = reverse_insertion_sort(n, lst)
    utils.write_file([res])