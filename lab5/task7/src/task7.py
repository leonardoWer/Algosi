"""
Пирамидальная сортировка в невозрастающем порядке
"""

from lab5 import utils
import os


CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def heapify(lst: list, n: int, i: int):
    """
    Проверяет, является ли поддерево с корнем в i кучей
    Если нет, она перестраивает его так, чтобы оно стало кучей
    Это делается рекурсивно для дочерних элементов
    """
    smallest = i  # Инициализируем корень дерева как самый маленький элемент
    left = 2 * i + 1  # левый элемент
    right = 2 * i + 2  # правый элемент

    # Если левый элемент меньше корня
    if left < n and lst[left] < lst[smallest]:
        smallest = left

    # Если правый элемент меньше самого маленького элемента
    if right < n and lst[right] < lst[smallest]:
        smallest = right

    # Если самый маленький элемент не корень
    if smallest != i:
        lst[i], lst[smallest] = lst[smallest], lst[i]

        # Рекурсивно хипифай для затронутого поддерева
        heapify(lst, n, smallest)


def heap_sort(n: int, lst: list) -> list:
    """
    Пирамидальная сортировка или сортировка кучей
     - Сначала строится куча из массива
     - Извлекаются элементы из кучи
     - Самый маленький элемент (корень) перемещается в конец массива и вызывается heapify для уменьшенной кучи.
    """
    # Построение кучи
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)

    # Извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]  # Перемещаем текущий корень в конец
        heapify(lst, i, 0)  # Вызываем хипифай на уменьшенной куче

    return lst


def input_data():
    data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    n, lst = int(data[0]), utils.str_to_list(data[1])

    return n, lst


def main():
    n, lst = input_data()
    result = heap_sort(n, lst)

    return result


if __name__ == "__main__":
    result = main()

    utils.write_file(CURRENT_SCRIPT_DIR_PATH, [result])
