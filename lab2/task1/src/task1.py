"""
Сортировка слиянием
"""
from lab2 import utils


def merge_sort(lst: list) -> list:
    """
    Рекурсивная функция
    - Разбивает массив на маленькие части, чтобы сократить количество операций
    - Сортирует каждую часть
    - Возвращает отсортированный массив, с помощью процедуры merge
    """
    n = len(lst)
    n1 = n // 2  # Выбираем первую половину массива
    lst1 = lst[:n1]  # Делим массив на два, примерно равной длины
    lst2 = lst[n1:]
    if len(lst1) > 1:
        lst1 = merge_sort(lst1)
    if len(lst2) > 1:
        lst2 = merge_sort(lst2)

    return merge(lst1, lst2)  # Если делить больше некуда, объединяем списки


def merge(lst1: list, lst2: list) -> list:
    """
    Сливает два отсортированных массива в один
    """
    res = []
    lst1_len = len(lst1)
    lst2_len = len(lst2)
    i, j = 0, 0  # Начинаем сравнивать элементы с 0
    while i < lst1_len and j < lst2_len:  # Пока не дойдём до конца списков
        if lst1[i] <= lst2[j]:
            res.append(lst1[i])
            i += 1  # Поскольку добавили предыдущий элемент, больше его не сравниваем
        else:
            res.append(lst2[j])
            j += 1
    res += lst1[i:] + lst2[j:]  # Добавляем оставшиеся элементы
    return res


if __name__ == "__main__":
    n, lst = utils.read_file()  # Количество элементов и список с элементами
    res = merge_sort(lst)
    utils.write_file([res])
