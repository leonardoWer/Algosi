from lab5.task7.src.task7 import *
from lab5 import utils
import datetime
import tracemalloc
import unittest
import random


class TaskTest7(unittest.TestCase):

    def test_func_performance(self):
        """Тест на время и память"""
        # given
        n = 21
        lst = utils.str_to_list("42 23 16 15 8 4 6 5 4 3 2 1 2 3 1000000000 100000000 10000000 1000000 100 1000 12873891")

        # when
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        result = heap_sort(n, lst)

        finish_time = datetime.datetime.now()
        spent_time = finish_time - start_time  # Итоговое время

        current, peak = tracemalloc.get_traced_memory()
        memory_used = current / 10 ** 6

        # then
        self.assertEqual(result, [1000000000,100000000,12873891,10000000,1000000,1000,100,42,23,16,15,8,6,5,4,4,3,3,2,2,1])

    # Тест сортировки на худших данных
    def test_heap_sort_hard(self):
        """Тест сортировки на самых больших данных"""
        # given
        n_hud = 10 ** 5
        lst_hud = [random.randint(10**3, 10 ** 9) for i in range(n_hud)]

        # when
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        result = heap_sort(n_hud, lst_hud)

        finish_time = datetime.datetime.now()
        spent_time = finish_time - start_time  # Итоговое время

        current, peak = tracemalloc.get_traced_memory()
        memory_used = current / 10 ** 6

        # then
        self.assertEqual(lst_hud, sorted(lst_hud, reverse=True))
        print(f"\nНа самых больших данных сортировка отработала за {spent_time} с, использовав памяти {memory_used} Мб")

    # Тест сортировки на средних данных
    def test_heap_sort_middle(self):
        """Тест сортировки на средних данных"""
        # given
        n_mid = 10 ** 3
        lst_mid = [random.randint(1, 10 ** 9) for i in range(n_mid)]

        # when
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        result = heap_sort(n_mid, lst_mid)

        finish_time = datetime.datetime.now()
        spent_time = finish_time - start_time  # Итоговое время

        current, peak = tracemalloc.get_traced_memory()
        memory_used = current / 10 ** 6

        # then
        self.assertEqual(lst_mid, sorted(lst_mid, reverse=True))
        print(f"\nНа средних данных сортировка отработала за {spent_time} с, использовав памяти {memory_used} Мб")


if __name__ == "__main__":
    unittest.main()
