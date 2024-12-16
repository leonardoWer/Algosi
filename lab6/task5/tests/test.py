from lab6.task5.src.task5 import *
from lab6 import utils
import unittest
import datetime
import tracemalloc


class TaskTest5(unittest.TestCase):

    def test_func_performance(self):
        """Тест функции на время и память"""
        # given
        candidates_list = ['McCain 10', 'McCain 5', 'Obama 9', 'Obama 8', 'McCain 1']

        max_allowed_time = datetime.timedelta(seconds=2)  # Задаю ограничение по времени

        # when
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        result = calculate_election_results(candidates_list)

        finish_time = datetime.datetime.now()
        spent_time = finish_time - start_time  # Итоговое время

        current, peak = tracemalloc.get_traced_memory()
        memory_used = current / 10 ** 6

        # then
        self.assertEqual(result, ['McCain 16', 'Obama 17'])
        self.assertLessEqual(spent_time, max_allowed_time)
        self.assertLessEqual(memory_used, 256)

    def test_func_correctly(self):
        """Тест на корректность работы"""
        # given
        candidates_list1 = ['McCain 10', 'McCain 5', 'Obama 9', 'Obama 8', 'McCain 1']
        candidates_list2 = ['ivanov 100', 'ivanov 500', 'ivanov 300', 'petr 70', 'tourist 1', 'tourist 2']
        candidates_list3 = ['bur 1']

        # when
        result1 = calculate_election_results(candidates_list1)
        result2 = calculate_election_results(candidates_list2)
        result3 = calculate_election_results(candidates_list3)

        # then
        self.assertEqual(result1, ['McCain 16', 'Obama 17'])
        self.assertEqual(result2, ['ivanov 900', 'petr 70', 'tourist 3'])
        self.assertEqual(result3, ['bur 1'])


if __name__ == "__main__":
    unittest.main()
