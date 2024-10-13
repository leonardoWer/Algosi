"""
Бинарный поиск
"""

file_in = open("../txtfiles/input.txt")
file_out = open("../txtfiles/output.txt", "w")

a = list(map(int, file_in.readline().split()))
b = list(map(int, file_in.readline().split()))

n = a[0]  # Количество элементов массива
a.remove(a[0])  # Массив

k = b[0]  # Количество элементов поиска
b.remove(k)  # Элементы поиска

def bin_search(n: int, lst: list, k: int, find_el_list: list) -> str:
    """
    - Делим массив на маленькие части, среди которых выполняем поиск
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
    res = [str(el) for el in res]
    return " ".join(res)


file_out.write(bin_search(n, a, k, b))
