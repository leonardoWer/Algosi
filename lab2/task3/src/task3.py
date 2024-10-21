"""
Алгоритм подсчёта количества инверсий
"""

file_in = open("../txtfiles/input.txt")
file_out = open("../txtfiles/output.txt", "w")

n = int(file_in.readline())  # Количество элементов
lst = list(map(int, file_in.readline().split()))  # Список с элементами

def find_inverse(n:int, lst:list)->str:
    """
    Функция находит количество инверсий в списке, используя сортировку слиянием
    """
    cnt_inverse = merge_sort(lst,0,n-1)

    return str(cnt_inverse)


def merge_sort(lst: list, left: int, right: int)->int:
    """
     Рекурсивная функция
    """
    cnt = 0
    if left < right:
        # Находим середину
        mid = (right + left) // 2
        # Рекурсивно разделяем массив
        cnt += merge_sort(lst, left, mid)
        cnt += merge_sort(lst, mid + 1, right)
        # Сливаем массив
        cnt += merge(lst, left, mid, right)

    return cnt


def merge(lst: list, left: int, mid: int, right: int)->int:
    """
    Сливает два отсортированных массива в один
    """
    cnt = 0
    n1 = mid - left + 1
    n2 = right - mid
    left_lst = [0]*n1
    right_lst = [0]*n2
    # Заполняем левый список
    for i in range(0, n1):
        left_lst[i] = lst[left+i]
    # Заполняем правый список
    for j in range(0,n2):
        right_lst[j] = lst[mid+j+1]
    i, j = 0,0
    k = left
    # Сортируем элементы
    while i<n1 and j<n2:
        if left_lst[i] <= right_lst[j]:
            lst[k] = left_lst[i]
            i += 1
        else:
            lst[k] = right_lst[j]
            j += 1
            cnt += (n1-i) # Добавляем к счётчику инверсий все случаи, когда текущий элемент больше последующих
        k += 1

    # Добавляем оставшиеся элементы
    while i<n1:
        lst[k] = left_lst[i]
        i += 1
        k += 1
    while j<n2:
        lst[k] = right_lst[j]
        j += 1
        k += 1

    return cnt


file_out.write(find_inverse(n, lst))