"""
Пузырьковая сортировка
"""

file_in = open("../txtfiles/input.txt")
file_out = open("../txtfiles/output.txt", "w")

n = int(file_in.readline()) #Количество элементов
lst = list(map(int, file_in.readline().split())) #Список с элементами

def bubble_sort(n:int, lst:list) ->str:
    """
    - Проходимся по всем парам элементов массива
    - Если элементы в невозрастающем порядке - меняем их местами
    - Переходим к следующей паре
    """
    for i in range(n-1):
        for j in range(i+1, n):
            if lst[j] <= lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
    lst = [str(el) for el in lst]
    return " ".join(lst)


file_out.write(bubble_sort(n, lst))