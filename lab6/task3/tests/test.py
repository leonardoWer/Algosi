from lab6.task3.src.task3 import *
from lab6 import utils
import unittest
import datetime
import tracemalloc


class TaskTest3(unittest.TestCase):

    def test_func_performance(self):
        """Тест функции на время и память"""
        # given
        m, n, requests = 3, 12, ['check 0', 'find help', 'add help', 'add del', 'add add', 'find add', 'find del', 'del del', 'find del', 'check 0', 'check 1', 'check 2']

        max_allowed_time = datetime.timedelta(seconds=7)  # Задаю ограничение по времени

        # when
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        result = commands_to_actions(m, n, requests)

        finish_time = datetime.datetime.now()
        spent_time = finish_time - start_time  # Итоговое время

        current, peak = tracemalloc.get_traced_memory()
        memory_used = current / 10 ** 6

        # then
        self.assertEqual(result, ['', 'no', 'yes', 'yes', 'no', '', 'add help', ''])
        self.assertLessEqual(spent_time, max_allowed_time)
        self.assertLessEqual(memory_used, 512)


    def test_func_correctly(self):
        """Тест на корректность работы"""
        # given
        m1, n1, requests1 = 5, 12, ['add world', 'add HellO', 'check 4', 'find World', 'find world', 'del world', 'check 4', 'del HellO', 'add luck', 'add GooD', 'check 2', 'del good']
        m2, n2, requests2 = 4, 8, ['add test', 'add test', 'find test', 'del test', 'find test', 'find Test', 'add Test', 'find Test']
        m3, n3, requests3 = 3, 12, ['check 0', 'find help', 'add help', 'add del', 'add add', 'find add', 'find del', 'del del', 'find del', 'check 0', 'check 1', 'check 2']

        # when
        result1 = commands_to_actions(m1, n1, requests1)
        result2 = commands_to_actions(m2, n2, requests2)
        result3 = commands_to_actions(m3, n3, requests3)

        # then
        self.assertEqual(result1, ['HellO world', 'no', 'yes', 'HellO', 'GooD luck'])
        self.assertEqual(result2, ['yes', 'no', 'no', 'yes'])
        self.assertEqual(result3, ['', 'no', 'yes', 'yes', 'no', '', 'add help', ''])


if __name__ == "__main__":
    unittest.main()
