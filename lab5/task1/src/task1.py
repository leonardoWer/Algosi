"""
Куча ли?
"""

from lab5 import utils
import os


CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def is_heap(n:int, lst:list) -> str:
    for i in range(1, n + 1):
        left_child_index = 2 * i
        right_child_index = 2 * i + 1

        if left_child_index <= n:
            if lst[i - 1] > lst[left_child_index - 1]:
                return "NO"

        if right_child_index <= n:
            if lst[i - 1] > lst[right_child_index - 1]:
                return "NO"

    return "YES"


def main():
    n, lst = input_data()
    result = is_heap(n, lst)
    return result


def input_data() -> (int, list):
    data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    n, lst = int(data[0]), utils.str_to_list(data[1])
    return n, lst


if __name__ == "__main__":
    result = main()
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, [result])
