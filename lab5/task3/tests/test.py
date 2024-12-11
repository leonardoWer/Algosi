from lab5.task3.src.task3 import *
from lab5 import utils
import datetime
import tracemalloc
import unittest


class TaskTest3(unittest.TestCase):

    def test_func_performance(self):
        """Тест на время и память"""
        # given
        s, n, packets_info = 3, 6, [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2]]
        max_allowed_time = datetime.timedelta(seconds=10)  # Задаю ограничение по времени

        # when
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        result = process_packets(s, n, packets_info)

        finish_time = datetime.datetime.now()
        spent_time = finish_time - start_time  # Итоговое время

        current, peak = tracemalloc.get_traced_memory()
        memory_used = current / 10 ** 6

        # then
        self.assertEqual(result, [0, 2, 4, 6, 8, -1])
        self.assertLessEqual(spent_time, max_allowed_time)
        self.assertLessEqual(memory_used, 512)

    def test_func_correctly(self):
        """Тест на корректность работы"""
        # given
        s1, n1, packets_info1 = 1, 0, []
        s2, n2, packets_info2 = 1, 1, [[0,0]]
        s3, n3, packets_info3 = 1, 2, [[0,1], [0,1]]
        s4, n4, packets_info4 = 1, 2, [[0,1], [1,1]]
        s12, n12, packets_info12 = 3, 6, [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2]]

        # when
        result1 = process_packets(s1, n1, packets_info1)
        result2 = process_packets(s2, n2, packets_info2)
        result3 = process_packets(s3, n3, packets_info3)
        result4 = process_packets(s4, n4, packets_info4)
        result12 = process_packets(s12, n12, packets_info12)

        # then
        self.assertEqual(result1, [])
        self.assertEqual(result2, [0])
        self.assertEqual(result3, [0, -1])
        self.assertEqual(result4, [0, 1])
        self.assertEqual(result12, [0, 2, 4, 6, 8, -1])


if __name__ == "__main__":
    unittest.main()
