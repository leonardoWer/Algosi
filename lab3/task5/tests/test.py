from lab3.task5.src.task5 import index_harsh
from lab3 import utils
import unittest


class TaskTest2(unittest.TestCase):

    # Тест функции быстрой сортировки на данных из примера
    def test_quick_sort(self):
        """Тест быстрой сортировки на данных из примера"""
        # given
        lst1 = utils.read_file_1_list()
        lst2 = [1, 3, 1]

        # when
        utils.test_memory_and_time_lst(lst1, index_harsh, True)

        # then
        self.assertEqual(index_harsh(lst1), 3)
        self.assertEqual(index_harsh(lst2), 1)


if __name__ == "__main__":
    unittest.main()
