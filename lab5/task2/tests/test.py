from lab5.task2.src.task2 import *
from lab5 import utils
import datetime
import tracemalloc
import unittest


class TaskTest2(unittest.TestCase):

    def test_is_heap_performance(self):
        """Тест функции на время и память"""
        # given
        n, parents = 5, utils.str_to_list("4 -1 4 1 1")
        max_allowed_time = datetime.timedelta(seconds=3)  # Задаю ограничение по времени

        # when
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        tree, root = build_tree(n, parents)
        tree_height = find_tree_height(tree, root)

        finish_time = datetime.datetime.now()
        spent_time = finish_time - start_time  # Итоговое время

        current, peak = tracemalloc.get_traced_memory()
        memory_used = current / 10 ** 6

        # then
        self.assertEqual(tree_height, 3)
        self.assertLessEqual(spent_time, max_allowed_time)
        self.assertLessEqual(memory_used, 512)

    def test_is_heap_correctly(self):
        """Тест на корректность работы"""
        # given
        n1, parents1 = 5, utils.str_to_list("4 -1 4 1 1")
        n2, parents2 = 5, utils.str_to_list("-1 0 4 0 3")

        # when
        tree1, root1 = build_tree(n1, parents1)
        tree_height1 = find_tree_height(tree1, root1)
        tree2, root2 = build_tree(n2, parents2)
        tree_height2 = find_tree_height(tree2, root2)

        # then
        self.assertEqual(tree_height1, 3)
        self.assertEqual(tree_height2, 4)


if __name__ == "__main__":
    unittest.main()
