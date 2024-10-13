"""
Сортировка вставкой базовая
"""

file_in = open("../txtfiles/input.txt")
file_out = open("../txtfiles/output.txt", "w")

n = int(file_in.readline()) #Количество элементов
lst = list(map(int, file_in.readline().split())) #Список с элементами

def insertion_sort(n:int, lst:list) ->str:
    """
    - Проходимся по элементам массива, выбирам ключ
    - Сравниваем элементы, исходя из чего подбираем предполагаемую позицию
    - Ставим элемент на выбранный для него индекс
    """
    for i in range(1, n):
        key = lst[i]
        j = i-1
        while (j>=0) and (lst[j]>key):
            lst[j+1] = lst[j]
            j -=1
        lst[j+1] = key
    lst = [str(el) for el in lst]
    return " ".join(lst)

file_out.write(insertion_sort(n, lst))