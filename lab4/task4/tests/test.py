from lab4.task4.src.task4 import BracketChecker
from lab4 import utils
import unittest
import tracemalloc
import datetime
import os


CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

class TaskTest4(unittest.TestCase):

    def test_sort(self):
        """Тест на данных из примера"""
        # given
        bracket_checker = BracketChecker()
        lines_lst = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
        max_allowed_time = datetime.timedelta(seconds=5)  # Задаю ограничение по времени
        result = []

        # when
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        for line in lines_lst:
            result.append(bracket_checker.check(line))

        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        spent_time = finish_time - start_time  # Итоговое время

        current, peak = tracemalloc.get_traced_memory()
        memory_used = current / 10 ** 6

        # then

        self.assertEqual(result, ['Success', 'Success', 'Success', 'Success', 1, 3, 'Success', 10])
        self.assertLessEqual(spent_time, max_allowed_time)
        self.assertLessEqual(memory_used, 256)


if __name__ == "__main__":
    unittest.main()
