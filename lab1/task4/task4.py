"""
Линейный поиск
"""

file_in = open("input.txt")
file_out = open("output.txt", "w")

a = list(map(int, file_in.readline().split()))
v = int(file_in.readline())

def line_search(lst: list, find_el: int):
    len_lst = len(lst)
    cnt_el = 0
    ind_list = []
    for i in range(len_lst):
        if lst[i] == find_el:
            cnt_el+=1
            ind_list.append(i)
    if len(ind_list) >1:
        return f"Cnt v: {len(ind_list)}\nIndex's v: {",".join([str(el) for el in ind_list])}"
    elif len(ind_list) == 1:
        return ind_list[0]
    return -1

file_out.write(str(line_search(a, v)))
