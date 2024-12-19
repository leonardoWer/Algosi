"""
Точки и отрезки
"""

from lab3 import utils
import os


CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def make_lottery_data(file_name:str) -> (int, int, list[int], list[int]):
    """
    Обрабатывает входной файл
     - В первой строке файла содержаться: (s - количество интервалов, p - количество точек)
     - В последующих s строках файла содержаться: ([a, b] - интервал)
     - В последней строке файла содержаться: (dot_i, i от 1 до p)
     Возвращает (количество интервалов, количество точек, полный список всех интервалов, список с точками)
    """
    relative_path = f"../txtfiles/{file_name}.txt"
    file_path = os.path.join(CURRENT_SCRIPT_DIR_PATH, relative_path)
    file_in = open(file_path, "r")
    cnt_segment, cnt_dot = map(int, file_in.readline().split())
    list_with_segments, list_with_dots = [], []

    for segment in range(cnt_segment):
        a, b = map(int, file_in.readline().split())
        if a < b:
            for el in (list(range(a, b + 1))):
                list_with_segments.append(int(el))
        else:
            for el in (list(range(b, a + 1))):
                list_with_segments.append(int(el))

    list_with_dots = list(map(int, file_in.readline().split()))
    file_in.close()

    return cnt_segment, cnt_dot, list_with_segments, list_with_dots


def lottery_find(list_with_segments:list, list_with_dots:list) -> list:
    """
    Функция подсчитывает сколько раз точка встречалась в интервалах
     - Используется линейный поиск
     - Принимает список с интервалами(числа) и список с точками(числа)
     - Выводит список с числами - количество раз, которые встречается каждая точка
    """
    res = []
    for find_el in list_with_dots:
        cnt_found_dot_in_segments = line_search(list_with_segments, find_el)
        res.append(cnt_found_dot_in_segments)

    return res


def line_search(lst: list, find_el: int) -> int:
    """
    Функция линейного поиска
     - Возвращает количество раз, которые элемент встречается в списке
    """
    len_lst = len(lst)
    cnt_el = 0
    for i in range(len_lst):
        if lst[i] == find_el:
            cnt_el+=1

    return cnt_el


def input_data():
    cnt_segment, cnt_dot, list_with_segments, list_with_dots = make_lottery_data("input")
    cnt_segment_2, cnt_dot_2, list_with_segments_2, list_with_dots_2 = make_lottery_data("input2")
    cnt_segment_3, cnt_dot_3, list_with_segments_3, list_with_dots_3 = make_lottery_data("input3")

    return cnt_segment, cnt_dot, list_with_segments, list_with_dots, cnt_segment_2, cnt_dot_2, list_with_segments_2, list_with_dots_2, cnt_segment_3, cnt_dot_3, list_with_segments_3, list_with_dots_3


def main():
    cnt_segment, cnt_dot, list_with_segments, list_with_dots, cnt_segment_2, cnt_dot_2, list_with_segments_2, list_with_dots_2, cnt_segment_3, cnt_dot_3, list_with_segments_3, list_with_dots_3 = input_data()
    res1 = lottery_find(list_with_segments, list_with_dots)
    res2 = lottery_find(list_with_segments_2, list_with_dots_2)
    res3 = lottery_find(list_with_segments_3, list_with_dots_3)

    result = ["input 1:", res1, "\ninput 2:", res2, "\ninput 3:", res3]
    return result


if __name__ == "__main__":
    result = main()
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, result)
