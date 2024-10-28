"""
Бинарный поиск
"""

from lab2 import utils


def bin_search(n: int, lst: list, k: int, find_el_list: list) -> list:
    """
    - Делим массив на маленькие части, среди которых выполняем поиск
    - Находим серединный элемент, сравниваем с тем, что ищем
    - Сужаем границы поиска до тех пор, пока не найдём совпадение
    - Если совпадений нет - возвращаем -1
    """
    res = []  # Список с индексами
    for el in find_el_list:  # Перебираем элементы, индексы которых ищем в списке
        el_is_find = False
        low = 0
        high = n - 1
        while low <= high and not el_is_find:
            mid = (low + high) // 2  # Находим средний элемент
            if lst[mid] == el:
                res.append(mid)
                el_is_find = True
            # Сужаем границы поиска
            elif lst[mid] > el:
                high = mid - 1
            elif lst[mid] < el:
                low = mid + 1
        if not el_is_find:
            res.append(-1)

    return res


if __name__ == "__main__":
    n, a, k, b = utils.read_file_4()
    res = bin_search(n, a, k, b)
    utils.write_file([res])
