file_in = open("input.txt")
file_out = open("output.txt", "w")

n = int(file_in.readline()) #Количество элементов
lst = [int(el) for el in file_in] #Список с элементами

def insertion_sort(n:int, lst:list) ->str:
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