"""
Пузырьковая сортировка
"""

from lab1 import utils


def bubble_sort(n:int, lst:list) -> list:
    """
    Функция сортировки пузырьком
     Принимает: (кол-во элементов, список)
     Возвращает: отсортированный список
    - Проходимся по всем парам элементов массива
    - Если элементы в невозрастающем порядке - меняем их местами
    - "Всплывает" наибольший элемент
    """
    for i in range(n-1):
        for j in range(i+1, n):
            if lst[j] <= lst[i]:
                lst[j], lst[i] = lst[i], lst[j]

    return lst


if __name__ == "__main__":
    n, lst = utils.read_file()
    res = bubble_sort(n, lst)
    utils.write_file([res])