"""
Сортировка выбором
"""

file_in = open("input.txt")
file_out = open("output.txt", "w")

n = int(file_in.readline()) # Количество элементов
lst = list(map(int, file_in.readline().split())) # Список с элементами

def selection_sort(n: int, lst: list) -> str:
    lst_copy = lst[:]
    res = [min(lst)]
    lst_copy.remove(min(lst))
    for i in range(n-1):
        res.append(min(lst_copy))
        lst_copy.remove(min(lst_copy))
    res += lst_copy
    res = [str(el) for el in res]
    return " ".join(res)

file_out.write(selection_sort(n, lst))
