from lab7 import utils
import os
from collections import deque

CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def find_min_operations(n: int) -> list:
    # Массив для хранения минимального количества операций до каждого числа
    operations = [float('inf')] * (n + 1)
    # Массив для хранения предшественников
    predecessor = [-1] * (n + 1)

    # Начальные условия
    operations[1] = 0
    queue = deque([1])

    while queue:
        current = queue.popleft()

        # Возможные следующие шаги
        next_steps = [current + 1, current * 2, current * 3]

        for next_num in next_steps:
            if next_num <= n and operations[next_num] == float('inf'):
                operations[next_num] = operations[current] + 1
                predecessor[next_num] = current
                queue.append(next_num)

    path = []  # Путь от n к 1
    step = n
    while step != -1:
        path.append(step)
        step = predecessor[step]

    path.reverse()  # Переворачиваем путь, чтобы получить от 1 до n

    return [operations[n], path]


def input_data():
    data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    n = int(data[0])
    return n


def main():
    n = input_data()
    result = find_min_operations(n)
    return result


if __name__ == "__main__":
    result = main()
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, result)
