"""
В графстве Сортленда нужно найти 3х человек
- Самого бедного
- Среднего достатка
- Самого богатого
"""

file_in = open("../txtfiles/input.txt")
file_out = open("../txtfiles/output.txt", "w")

n = int(file_in.readline())  # Количество жителей
m = list(map(float, file_in.readline().split()))  # Список с состоянием житиелей, индексы жителей i+1

def Sortland(n: int, m: list) -> str:
    win_list = []

    win_list.append(m.index(min(m)) + 1)
    m_sort = sorted(m)
    win_list.append(m.index(m_sort[len(m_sort) // 2]) + 1)
    win_list.append(m.index(max(m)) + 1)

    win_list = [str(el) for el in win_list]
    return " ".join(win_list)

file_out.write(Sortland(n,m))
