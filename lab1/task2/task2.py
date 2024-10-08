"""
Сортировка вставкой +, дополнительно выводит номер, на который был поставлен элемент при обработке
"""

file_in = open("input.txt")
file_out = open("output.txt", "w")

n = int(file_in.readline())  # Количество элементов
lst = list(map(int, file_in.readline().split()))  # Список с элементами

def insertion_sort(n:int, lst:list) -> str:
    indexes = "1 "
    for i in range(1, n):
        key = lst[i]
        j = i-1
        while (j>=0) and (lst[j]>key):
            lst[j+1] = lst[j]
            j -=1
        lst[j+1] = key
        indexes+=str(j+1+1)+" "

    lst = [str(el) for el in lst]
    res = indexes+"\n"+ " ".join(lst)
    return res

file_out.write(insertion_sort(n, lst))