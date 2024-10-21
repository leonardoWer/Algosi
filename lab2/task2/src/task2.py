"""
Сортировка слиянием +
"""

file_in = open("../txtfiles/input.txt")
file_out = open("../txtfiles/output.txt", "w")

n = int(file_in.readline())  # Количество элементов
lst = list(map(int, file_in.readline().split()))  # Список с элементами


def merge_sort(lst: list, left: int, right: int)->list:
    """
     - Рекурсивная функция
    """
    if left < right:
        # Находим середину
        mid = (right + left) // 2
        # Рекурсивно разделяем массив
        merge_sort(lst, left, mid)
        merge_sort(lst, mid + 1, right)
        # Сливаем массив
        merge(lst, left, mid, right)

        if __name__ == "__main__":
            add_merge_description(left+1, right+1, lst[left], lst[right])
        else:
            print(left+1, right+1, lst[left], lst[right])

    return lst

def merge(lst: list, left: int, mid: int, right: int):
    """
    Сливает два отсортированных массива в один
    """
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


def add_merge_description(i: int, j: int, v_i: int, v_j: int):
    """
    Записывает в файл промежуточные операции сортировки слиянием
    """
    file_out.write(f"{i} {j} {v_i} {v_j}\n")

if __name__ == "__main__":
    res = " ".join([str(el) for el in merge_sort(lst, 0, n-1)])  # Список с результатом приводим к строке и записываем в файл
    file_out.write(res)
