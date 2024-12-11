"""
Высота дерева
"""

from lab5 import utils
import os


CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def build_tree(n:int, parents:list):
    """
    Cоздает список смежности для дерева
    Каждый индекс в списке представляет узел, а значения — его дочерние узлы
    Находит корень дерева
    """
    tree = [[] for i in range(n)]
    root = None
    for child in range(n):
        parent = parents[child]
        if parent == -1:
            root = child
        else:
            tree[parent].append(child)
    return tree, root


def find_tree_height(tree:list[list], node:int):
    """
    Рекурсивно вычисляет высоту дерева
     - Если узел не имеет детей - возвращает 1
     - Для каждого дочернего узла рекурсивно вызывается функция и находится максимальная высота из дочерних узлов
     """
    if not tree[node]:  # Если у узла нет детей
        return 1
    else:
        height = 0
        for child in tree[node]:
            height = max(height, find_tree_height(tree, child))
        return height + 1


def input_data() -> (int, list):
    data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    cnt_nodes, parents = int(data[0]), utils.str_to_list(data[1])
    return cnt_nodes, parents


def main():
    cnt_nodes, parents = input_data()
    tree, root = build_tree(cnt_nodes, parents)
    tree_height = find_tree_height(tree, root)

    return tree_height


if __name__ == "__main__":
    result = main()
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, [result])
