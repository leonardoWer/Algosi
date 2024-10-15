"""
Сортировка слиянием +
"""

file_in = open("../txtfiles/input.txt")
file_out = open("../txtfiles/output.txt", "w")

n = int(file_in.readline())  # Количество элементов
lst = list(map(int, file_in.readline().split()))  # Список с элементами


def merge_sort(lst: list, left: int, right: int) -> list:
    """

    """
    if left < right:
        mid = (right + left) // 2
        merge_sort(lst, left, mid)
        merge_sort(lst, mid + 1, right)
        merge(lst, left, mid, right)

    return lst


def merge(lst: list, left: int, mid: int, right: int) -> list:
    """
    Сливает два отсортированных массива в один
    """
    left_lst = lst[left:mid + 1]
    right_lst = lst[mid + 1:right + 1]

    left_ind, right_ind = 0, 0

    for k in range(left, right + 1):
        if left_ind < len(left_lst) and right_ind < len(right_lst):
            if left_lst[left_ind] <= right_lst[right_ind]:
                lst[k] = left_lst[left_ind]
                left_ind += 1
            else:
                lst[k] = right_lst[right_ind]
                right_ind += 1

        elif left_ind < len(left_lst):
            lst[k] = left_lst[left_ind]
            left_ind += 1
        else:
            lst[k] = right_lst[right_ind]
            right_ind += 1

    add_merge_description(left + 1, right + 1, lst[left], lst[right])
    return lst


def add_merge_description(i: int, j: int, v_i: int, v_j: int):
    """
    Записывает в файл промежуточные операции сортировки слиянием
    """
    file_out.write(f"{i} {j} {v_i} {v_j}\n")


res = " ".join(
    [str(el) for el in merge_sort(lst, 0, n - 1)])  # Список с результатом приводим к строке и записываем в файл
file_out.write(res)
