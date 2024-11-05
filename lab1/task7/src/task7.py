"""
В графстве Сортленда нужно найти 3-х человек
- Самого бедного
- Среднего достатка
- Самого богатого
"""

from lab1 import utils


def Sortland(n: int, m: list) -> list:
    """ Графство Сортленд """
    win_list = []

    win_list.append(m.index(min(m)) + 1)
    m_sort = sorted(m)
    win_list.append(m.index(m_sort[len(m_sort) // 2]) + 1)
    win_list.append(m.index(max(m)) + 1)

    return win_list


if __name__ == "__main__":
    file_in = open("../txtfiles/input.txt")
    n = int(file_in.readline())  # Количество жителей
    m = list(map(float, file_in.readline().split()))  # Список с состоянием жителей, индексы жителей i+1

    res = Sortland(n, m)
    utils.write_file([res])
