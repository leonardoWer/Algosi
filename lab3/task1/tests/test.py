from lab3.task1.src.task1 import quick_sort, randomized_quick_sort
from lab3.task1.src.task2 import randomized_quick_sort_three
from lab3 import utils
import random
import unittest


class TaskTest(unittest.TestCase):

    # Тест функции быстрой сортировки на данных из примера
    def test_quick_sort(self):
        """Тест быстрой сортировки на данных из примера"""
        # given
        n, lst = utils.read_file()

        # when
        utils.test_memory_and_time_lst_n(lst, n, quick_sort, True)

        # then
        self.assertEqual(lst, [2, 2, 2, 3, 9])

    # Тест функции рандомной быстрой сортировки на данных из примера
    def test_randomized_quick_sort(self):
        """Тест рандомной быстрой сортировки на данных из примера"""
        # given
        n, lst = utils.read_file()

        # when
        utils.test_memory_and_time_lst_n(lst, n, randomized_quick_sort, True)

        # then
        self.assertEqual(lst, [2, 2, 2, 3, 9])

    # Тест функции рандомной быстрой сортировки с 3мя списками на данных из примера
    def test_randomized_quick_sort_three(self):
        """Тест рандомной быстрой тройной сортировки на данных из примера"""
        # given
        n, lst = utils.read_file()

        # when
        utils.test_memory_and_time_lst_n(lst, n, randomized_quick_sort_three, True)

        # then
        self.assertEqual(lst, [2, 2, 2, 3, 9])

    # Тест функции быстрой сортировки на худших данных
    def test_quick_sort_hard(self):
        """Тест быстрой сортировки на самых больших данных"""
        # given
        lst_hud = [random.randint(1, 10 ** 9) for i in range(10 ** 5)]
        n_hud = 10**5

        # when
        utils.test_memory_and_time_lst_n(lst_hud, n_hud, quick_sort, False)

        # then
        self.assertEqual(lst_hud, sorted(lst_hud))

    # Тест функции рандомной быстрой сортировки на худших данных
    def test_randomized_quick_sort_hard(self):
        """Тест рандомной быстрой сортировки на самых больших данных"""
        # given
        lst_hud = [random.randint(1, 10 ** 9) for i in range(10 ** 5)]
        n_hud = 10 ** 5

        # when
        utils.test_memory_and_time_lst_n(lst_hud, n_hud, randomized_quick_sort, False)

        # then
        self.assertEqual(lst_hud, sorted(lst_hud))

    # Тест функции рандомной быстрой сортировки с 3мя списками на худших данных
    def test_randomized_quick_sort_three_hard(self):
        """Тест рандомной быстрой тройной сортировки на самых больших данных"""
        # given
        lst_hud = [random.randint(1, 10 ** 9) for i in range(10 ** 5)]
        n_hud = 10 ** 5

        # when
        utils.test_memory_and_time_lst_n(lst_hud, n_hud, randomized_quick_sort_three, False)

        # then
        self.assertEqual(lst_hud, sorted(lst_hud))

    # Тест функции рандомной быстрой сортировки с 3мя списками на худших данных
    def test_three_quick_sorts(self):
        """Сравнение трёх быстрых сортировки на самых больших данных"""
        # given
        lst_hud = [random.randint(1, 10 ** 9) for i in range(10 ** 5)]
        n_hud = 10 ** 5
        res1, res2, res3 = lst_hud[:], lst_hud[:], lst_hud[:]

        # when
        utils.test_memory_and_time_lst_n(res1, n_hud, quick_sort, False)
        utils.test_memory_and_time_lst_n(res2, n_hud, randomized_quick_sort, False)
        utils.test_memory_and_time_lst_n(res3, n_hud, randomized_quick_sort_three, False)

        # then
        self.assertEqual(res1, sorted(res1))
        self.assertEqual(res2, sorted(res2))
        self.assertEqual(res3, sorted(res3))

    # Тест функции рандомной быстрой сортировки с 3мя списками на больших данных с большим количеством повторяющихся элементов и сравнение с быстрой сортировкой
    def test_randomized_quick_sort_three_hard_repeat(self):
        """Сравнение быстрых сортировок при одинаковых значениях"""
        # given
        lst_hud = [random.randint(1, 10 ** 9) for i in range(500)]
        lst_hud += [1 for i in range(500)]
        n_hud = 1000

        # when
        utils.test_memory_and_time_lst_n(lst_hud, n_hud, randomized_quick_sort_three, False)
        utils.test_memory_and_time_lst_n(lst_hud, n_hud, quick_sort, False)

        # then
        self.assertEqual(lst_hud, sorted(lst_hud))


if __name__ == "__main__":
    unittest.main()