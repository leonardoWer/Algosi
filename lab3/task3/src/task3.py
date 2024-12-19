"""
Сортировка Пугалом
"""

from lab3 import utils
import os


CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


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


def input_data():
    data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    n1, k1 = map(int, data[0].split())
    lst1 = utils.str_to_list(data[1])
    n2, k2 = map(int, data[2].split())
    lst2 = utils.str_to_list(data[3])
    return n1, k1, lst1, n2, k2, lst2

def main():
    n1, k1, lst1, n2, k2, lst2 = input_data()
    res1 = scarecrow_sort(n1, k1, lst1)
    res2 = scarecrow_sort(n2, k2, lst2)
    return [res1, res2]


if __name__ == "__main__":
    result = main()
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, result)
