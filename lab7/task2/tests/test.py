from lab7.task2.src.task2 import *
from lab7 import utils
import unittest
import datetime
import tracemalloc


class TaskTest2(unittest.TestCase):

    def test_func_performance(self):
        """Тест функции на время и память"""
        # given
        n = 96234

        max_allowed_time = datetime.timedelta(seconds=1)  # Задаю ограничение по времени

        # when
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        result = find_min_operations(n)

        finish_time = datetime.datetime.now()
        spent_time = finish_time - start_time  # Итоговое время

        current, peak = tracemalloc.get_traced_memory()
        memory_used = current / 10 ** 6

        # then
        self.assertEqual(result, [14, [1, 2, 6, 7, 21, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234]])
        self.assertLessEqual(spent_time, max_allowed_time)
        self.assertLessEqual(memory_used, 512)


    def test_func_correctly(self):
        """Тест на корректность работы"""
        # given
        n1 = 1
        n2 = 5
        n3 = 96234

        # when
        result1 = find_min_operations(n1)
        result2 = find_min_operations(n2)
        result3 = find_min_operations(n3)

        # then
        self.assertEqual(result1, [0, [1]])
        self.assertEqual(result2, [3, [1, 2, 4, 5]])
        self.assertEqual(result3, [14, [1, 2, 6, 7, 21, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234]])


if __name__ == "__main__":
    unittest.main()
