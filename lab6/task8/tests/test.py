from lab6.task8.src.task8 import *
from lab6 import utils
import datetime
import tracemalloc
import unittest


class TaskTest8(unittest.TestCase):

    def test_func_performance(self):
        """Тест функции на время и память"""
        # given
        n, x, a, b, ac, bc, ad, bd = 4, 0, 0, 0, 1, 1, 0, 0

        max_allowed_time = datetime.timedelta(seconds=5)  # Задаю ограничение по времени

        # when
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        result = hash_table_operations(n, x, a, b, ac, bc, ad, bd)

        finish_time = datetime.datetime.now()
        spent_time = finish_time - start_time  # Итоговое время

        current, peak = tracemalloc.get_traced_memory()
        memory_used = current / 10 ** 6

        # then
        self.assertEqual(result, [3, 1, 1])
        self.assertLessEqual(spent_time, max_allowed_time)
        self.assertLessEqual(memory_used, 256)


if __name__ == "__main__":
    unittest.main()
