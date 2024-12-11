from lab4 import utils
import datetime
import tracemalloc
import unittest

from lab5.task1.src.task1 import is_heap


class TaskTest1(unittest.TestCase):

    def test_is_heap_performance(self):
        """Тест функции на время и память"""
        # given
        n, lst = 5, utils.str_to_list("4 -1 4 1 1")
        max_allowed_time = datetime.timedelta(seconds=2)  # Задаю ограничение по времени

        # when
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        result = is_heap(n, lst)

        finish_time = datetime.datetime.now()
        spent_time = finish_time - start_time  # Итоговое время

        current, peak = tracemalloc.get_traced_memory()
        memory_used = current / 10 ** 6

        # then
        self.assertEqual(result, "NO")
        self.assertLessEqual(spent_time, max_allowed_time)
        self.assertLessEqual(memory_used, 256)


    def test_is_heap_correctly(self):
        """Тест на корректность работы"""
        # given
        n1, lst1 = 5, utils.str_to_list("4 -1 4 1 1")
        n2, lst2 = 5, utils.str_to_list("-1 0 4 0 3")

        # when
        result1 = is_heap(n1, lst1)
        result2 = is_heap(n2, lst2)

        # then
        self.assertEqual(result1, "NO")
        self.assertEqual(result2, "YES")


if __name__ == "__main__":
    unittest.main()