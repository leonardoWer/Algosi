"""
Сортировка выбором
"""

file_in = open("../txtfiles/input.txt")
file_out = open("../txtfiles/output.txt", "w")

n = int(file_in.readline()) # Количество элементов
lst = list(map(int, file_in.readline().split())) # Список с элементами

def selection_sort(n: int, lst: list) -> str:
    """
    - Проходимся по элементам массива, запоминаем элемент и его индекс
    - Выбираем минимальный и обновляем минимальный элемент и его индекс
    - Меняем минимальный элемент с первым местами
    """
    for i in range(n-1):
        key = lst[i] # Выбираем минимальный элемент
        min_ind = i
        for j in range(i+1, n):
            if key>lst[j]:
                key = lst[j]
                min_ind = j
        if min_ind != i: # Обмен значениями
            lst[i], lst[min_ind] = lst[min_ind], lst[i]
    lst = [str(el) for el in lst]
    return " ".join(lst)


file_out.write(selection_sort(n, lst))
