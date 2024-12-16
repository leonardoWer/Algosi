from lab6.task6.src.task6 import *
from lab6 import utils
import unittest
import datetime
import tracemalloc


class TaskTest6(unittest.TestCase):

    def test_func_performance(self):
        """Тест функции на время и память"""
        # given
        fib_numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]

        max_allowed_time = datetime.timedelta(seconds=2)  # Задаю ограничение по времени

        # when
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        result = is_fib_list(fib_numbers)

        finish_time = datetime.datetime.now()
        spent_time = finish_time - start_time  # Итоговое время

        current, peak = tracemalloc.get_traced_memory()
        memory_used = current / 10 ** 6

        # then
        self.assertEqual(result, ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes'])
        self.assertLessEqual(spent_time, max_allowed_time)
        self.assertLessEqual(memory_used, 128)


if __name__ == "__main__":
    unittest.main()
