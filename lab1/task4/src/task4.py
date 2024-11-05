"""
Линейный поиск
"""

from lab1 import utils


def line_search(lst: list, find_el: int):
    """
    Выполнеяет поиск индекса элемента в списке за линейное время
     - Принимает: (список с элементами, элемент, который нужно найти)
     - Если элемент 1: возвращает его индекс
     - Если элемент встречается более 1 раза: возвращает строку, в которой: (кол-во элемента, индексы элемента)
     - Если элемент не встречается: возвращает -1
    """
    len_lst = len(lst)
    cnt_el = 0
    ind_list = []
    for i in range(len_lst):
        if lst[i] == find_el:
            cnt_el+=1
            ind_list.append(i)
    if len(ind_list) >1:
        return f"Cnt v: {len(ind_list)}\nIndex's v: {", ".join([str(el) for el in ind_list])}"
    elif len(ind_list) == 1:
        return ind_list[0]

    return -1


if __name__ == "__main__":
    find_el, lst = utils.read_file()
    res = line_search(lst, find_el)
    utils.write_file([res])
