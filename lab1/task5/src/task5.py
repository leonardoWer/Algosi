"""
Сортировка выбором
"""

from lab1 import utils


def selection_sort(n: int, lst: list) -> list:
    """
    Функция сортировки выбором
     Принимает: (количество элементов в списке, список)
     Возвращает: отсортированный список
    - Проходимся по элементам массива, запоминаем элемент и его индекс
    - Выбираем минимальный и обновляем минимальный элемент и его индекс
    - Меняем минимальный элемент с первым местами
    """
    for i in range(n-1):
        key = lst[i] # Выбираем минимальный элемент
        min_ind = i
        for j in range(i+1, n):
            if key>lst[j]:
                key = lst[j]
                min_ind = j
        if min_ind != i: # Обмен значениями
            lst[i], lst[min_ind] = lst[min_ind], lst[i]

    return lst


if __name__ == "__main__":
    n, lst = utils.read_file()
    res = selection_sort(n, lst)
    utils.write_file([res])
