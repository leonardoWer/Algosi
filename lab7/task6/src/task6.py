from lab7 import utils
import os
from bisect import bisect_left


CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def find_lis(n: int, sequence: list) -> list:
    """
    Принимает последовательность и находит длину и саму наибольшую возрастающую подпоследовательность
    """
    if not sequence:
        return [0, []]

    tails = []  # Массив для хранения наименьших хвостов возрастающих подпоследовательностей (значение, индекс, длина)
    predecessors = [-1] * len(sequence)
    lengths = [0] * len(sequence)

    for i, num in enumerate(sequence):
        pos = bisect_left(tails, num, key=lambda x: x[0])

        if pos == len(tails):
            if tails:
                predecessors[i] = tails[-1][1]
                lengths[i] = tails[-1][2] + 1
            else:
                lengths[i] = 1
            tails.append((num, i, lengths[i]))
        else:
            if pos > 0 and tails[pos-1][0] < num:
                  predecessors[i] = tails[pos-1][1]
                  lengths[i] = tails[pos-1][2] + 1
            else:
                  lengths[i] = 1
            tails[pos] = (num, i,lengths[i])

    # Восстанавливаем последовательность
    max_len = 0
    end_index = -1
    for i, l in enumerate(lengths):
        if l > max_len:
            max_len = l
            end_index = i

    path = []
    current_index = end_index
    while current_index != -1:
        path.append(sequence[current_index])
        current_index = predecessors[current_index]

    path.reverse()

    return [max_len, path]


def input_data():
    data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    n, lst = int(data[0]), utils.str_to_list(data[1])
    return n, lst


def main():
    n, lst = input_data()
    result = find_lis(n, lst)
    return result


if __name__ == "__main__":
    result = main()
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, result)
