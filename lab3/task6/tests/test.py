from lab3.task6.src.task6 import *
from lab3 import utils
import unittest


class TaskTest2(unittest.TestCase):

    # Тест функции быстрой сортировки на данных из примера
    def test_quick_sort(self):
        """Тест быстрой сортировки на данных из примера"""
        # given
        n, m, lst_a, lst_b = read_input_file_2_numbers_2_lists()
        lst_c = get_data_c(lst_a, lst_b)

        # when
        utils.test_memory_and_time_lst(lst_c, sort_z_numbers, True)

        # then
        self.assertEqual(sort_z_numbers(lst_c), 51)


if __name__ == "__main__":
    unittest.main()
