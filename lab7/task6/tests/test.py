from lab7.task6.src.task6 import *
from lab7 import utils
import unittest
import datetime
import tracemalloc


class TaskTest6(unittest.TestCase):

    def test_func_performance(self):
        """Тест функции на время и память"""
        # given
        n, lst = 6, utils.str_to_list("3 29 5 5 28 6")

        max_allowed_time = datetime.timedelta(seconds=2)  # Задаю ограничение по времени

        # when
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        result = find_lis(n, lst)

        finish_time = datetime.datetime.now()
        spent_time = finish_time - start_time  # Итоговое время

        current, peak = tracemalloc.get_traced_memory()
        memory_used = current / 10 ** 6

        # then
        self.assertEqual(result, [3, [3, 5, 28]])
        self.assertLessEqual(spent_time, max_allowed_time)
        self.assertLessEqual(memory_used, 256)


if __name__ == "__main__":
    unittest.main()
