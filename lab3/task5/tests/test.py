from lab3.task5.src.task5 import index_harsh
from lab3 import utils
import unittest


class TaskTest5(unittest.TestCase):

    # Тест функции быстрой сортировки на данных из примера
    def test_quick_sort(self):
        """Тест быстрой сортировки на данных из примера"""
        # given
        lst1 = utils.str_to_list("3 0 6 1 5")
        lst2 = [1, 3, 1]

        # when
        utils.test_memory_and_time_lst(lst1, index_harsh, True)

        # then
        self.assertEqual(index_harsh(lst1), 3)
        self.assertEqual(index_harsh(lst2), 1)


if __name__ == "__main__":
    unittest.main()
