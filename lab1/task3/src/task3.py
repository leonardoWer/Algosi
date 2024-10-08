"""
Сортировка вставкой в невозрастающем(убывающем) порядке
"""

file_in = open("../txtfiles/input.txt")
file_out = open("../txtfiles/output.txt", "w")

n = int(file_in.readline())  # Количество элементов
lst = list(map(int, file_in.readline().split()))  # Список с элементами

def insertion_sort(n:int, lst:list) ->str:
    for i in range(1, n):
        key = lst[i]
        j = i-1
        while (j>=0) and (lst[j]<key): # Поменялся знак неравенства, теперь нам подходит случай, когда предыдущий элеиент меньше чем ключ
            lst[j+1] = lst[j]
            j -=1
        lst[j+1] = key
    lst = [str(el) for el in lst]
    return " ".join(lst)

file_out.write(insertion_sort(n, lst))