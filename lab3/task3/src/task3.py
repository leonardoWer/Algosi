"""
Сортировка Пугалом
"""

from lab3 import utils


def scarecrow_sort(n:int, k:int, lst:list) -> str:
    """
    Сортировка пугалом
     - Принимает: (количество элементов списка, возможное расстояние, список)
     - Возвращает: (ДА - если можно отсортировать список, НЕТ - если нельзя отсортировать список)
    """
    sort_list = sorted(lst)
    while lst != sort_list:
        swapped = False
        for i in range(n-k):
            if lst[i] > lst[i+k]:
                switch(lst, i, i+k)
                swapped = True
                if lst == sort_list:
                    return "YES"
        if not swapped:
            return "NO"


def switch(lst:list, i:int, j:int) -> list:
    """ Меняет местами элементы в списке по их индексам"""
    lst[i], lst[j] = lst[j], lst[i]
    return lst


if __name__ == "__main__":
    file_in = open("../txtfiles/input.txt")

    n1, k1 = map(int, file_in.readline().split())
    lst1 = list((map(int, file_in.readline().split())))

    n2, k2 = map(int, file_in.readline().split())
    lst2 = list((map(int, file_in.readline().split())))

    res1 = scarecrow_sort(n1, k1, lst1)
    res2 = scarecrow_sort(n2, k2, lst2)

    utils.write_file([res1, res2])
