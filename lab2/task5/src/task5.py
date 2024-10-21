"""
Поиск элемента, который встречается в списке более n/2 раз
"""

def find_el_bolsh(lst: list, n: int) -> str:
    """
    Функция записывает в файл результат поиска элемента большинства в списке:
    - Возвращает 1, если такой элемент есть
    - Возвращает 0, если такого элемента нет
    """
    el_bolsh = majority(lst, 0, n - 1)
    if el_bolsh != 0:
        return "1\n"
    return "0\n"


def majority(lst: list, left: int, right: int):
    """
    Функция поиска элемента большинства
    - Возвращает элемент большинства, если такой есть
    - Возвращает 0, если такого элемента нет
    """
    if left == right:
        return lst[left]

    mid = (right + left) // 2
    left_find_el = majority(lst, left, mid)
    right_find_el = majority(lst, mid + 1, right)

    if left_find_el == right_find_el:
        return left_find_el
    if count_el(lst, left, mid, left_find_el) == 1 or count_el(lst, mid + 1, right, right_find_el) == 1:
        return 0
    if count_el(lst, left, mid, left_find_el) > count_el(lst, mid + 1, right, right_find_el):
        return left_find_el
    else:
        return right_find_el


def count_el(lst: list, left: int, right: int, finding_el: int):
    cnt = 0
    for i in range(left, right + 1):
        if lst[i] == finding_el:
            cnt += 1
    return cnt

if __name__ == "__main__":
    file_in = open("../txtfiles/input.txt")
    file_out = open("../txtfiles/output.txt", "w")

    n = int(file_in.readline())  # Количество элементов в 1 примере
    lst = list(map(int, file_in.readline().split()))  # Список с элементами в 1 примере
    n2 = int(file_in.readline())  # Количество элементов во 2 примере
    lst2 = list(map(int, file_in.readline().split()))  # Список с элементами во 2 примере

    file_out.write(find_el_bolsh(lst, n)) # Результат 1 примера
    file_out.write(find_el_bolsh(lst2, n2)) # Результат 2 примера
