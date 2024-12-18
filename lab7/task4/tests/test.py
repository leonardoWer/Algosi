from lab7.task4.src.task4 import *
from lab7 import utils
import unittest
import tracemalloc
import datetime


class TaskTest4(unittest.TestCase):

    def test_func_performance(self):
        """Тест функции на время и память"""
        # given
        n1, lst1, n2, lst2 = 3, [2, 7, 5], 2, [2, 5]

        max_allowed_time = datetime.timedelta(seconds=1)  # Задаю ограничение по времени

        # when
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        result = longest_common_subsequence(n1, lst1, n2, lst2)

        finish_time = datetime.datetime.now()
        spent_time = finish_time - start_time  # Итоговое время

        current, peak = tracemalloc.get_traced_memory()
        memory_used = current / 10 ** 6

        # then
        self.assertEqual(result, 2)
        self.assertLessEqual(spent_time, max_allowed_time)
        self.assertLessEqual(memory_used, 512)

    def test_func_correctly(self):
        """Тест на корректность работы"""
        # given
        len_a1, a1, len_b1, b1 = 3, [2, 7, 5], 2, [2, 5]
        len_a2, a2, len_b2, b2 = 1, [7], 4, [1, 2, 3, 4]
        len_a3, a3, len_b3, b3 = 4, [2, 7, 8, 3], 4, [5, 2, 8, 7]

        # when
        result1 = longest_common_subsequence(len_a1, a1, len_b1, b1)
        result2 = longest_common_subsequence(len_a2, a2, len_b2, b2)
        result3 = longest_common_subsequence(len_a3, a3, len_b3, b3)

        # then
        self.assertEqual(result1, 2)
        self.assertEqual(result2, 0)
        self.assertEqual(result3, 2)


if __name__ == "__main__":
    unittest.main()
