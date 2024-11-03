from lab3.task2.src.task2 import anti_qsort
from lab3 import utils
import unittest


class TaskTest(unittest.TestCase):

    # Тест функции быстрой сортировки на данных из примера
    def test_quick_sort(self):
        """Тест быстрой сортировки на данных из примера"""
        # given
        n = utils.read_file_1()

        # when
        utils.test_memory_and_time_lst(n, anti_qsort, True)

        # then
        self.assertEqual(anti_qsort(n), [1, 3, 2])



if __name__ == "__main__":
    unittest.main()
