from lab7 import utils
from lab7.task1.src import *
import unittest
import tracemalloc
import datetime

from lab7.task1.src.task1 import min_coins


class TaskTest1(unittest.TestCase):

    def test_func_performance(self):
        """Тест функции на время и память"""
        # given
        money, k, coins_list = 2, 3, [1, 3, 4]

        max_allowed_time = datetime.timedelta(seconds=1)  # Задаю ограничение по времени

        # when
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        result = min_coins(money, coins_list)

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
        money, k, coins_list = 2, 3, [1, 3, 4]
        money2, k2, coins_list2 = 34, 3, [1, 3, 4]


        # when
        result1 = min_coins(money, coins_list)
        result2 = min_coins(money2, coins_list2)

        # then
        self.assertEqual(result1, 2)
        self.assertEqual(result2, 9)


if __name__ == "__main__":
    unittest.main()