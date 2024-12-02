"""
Поиск максимума в движущемся массиве
"""

from lab4 import utils
from collections import deque
import os


CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

def find_sliding_max(lst:list, n:int, m:int) -> list:
    """
    Находит максимум в движущемся списке
     - Принимает: список, длину списка, число окон
     - Возвращает: список с максимумами от 1 до n-m + 1
    """
    res = []
    d_queue = deque() # Двусторонняя очередь

    for i in range(n):
        if d_queue and d_queue[0] < i - m + 1: # Удаляем элементы за пределами окна
            d_queue.popleft()

        while d_queue and lst[d_queue[-1]] < lst[i]: # Удаляем элементы, которые меньше текущего
            d_queue.pop()

        d_queue.append(i) # Добавляем текущий элемент в очередь

        if i >= m - 1:
            res.append(lst[d_queue[0]]) # Если достигли размера окна, добавляем максимальное значение в результат

    return res

def read_input_file() -> (list, int, int):
    """Считываем специфический инпут"""
    data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    n = int(data[0]) # Длина списка
    lst = utils.str_to_list(data[1])
    m = int(data[-1]) # Ширина окна

    return lst, n, m


if __name__ == "__main__":
    lst, n, m = read_input_file()
    result = find_sliding_max(lst, n, m)
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, [result])


