"""
Анти-быстрая сортировка
"""

from lab3 import utils


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


if __name__ == "__main__":
    lst = utils.read_file_1_list()
    res = index_harsh(lst)
    utils.write_file([res])
