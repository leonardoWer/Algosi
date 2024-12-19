"""
Анти-быстрая сортировка
"""

from lab3 import utils
import os


CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def index_harsh(citations: list) -> int:
    """
    Индекс Хирша
     - Принимает: (список - каждая цифра списка - количество использований статьи)
     - Возвращает: (число - индекс Хирша учёного)
    """
    for h in range(len(citations), 0, -1):
        cnt_citation = 0
        for el in citations:
            if el >= h:
                cnt_citation += 1
        if cnt_citation >= h:
            return h


def input_data():
    data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    lst = utils.str_to_list(data[0])
    return lst


def main():
    lst = input_data()
    result = index_harsh(lst)
    return result


if __name__ == "__main__":
    result = main()
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, [result])
