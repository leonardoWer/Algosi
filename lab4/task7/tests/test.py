from lab4 import utils
import unittest
from lab4.task7.src.task7 import find_sliding_max, read_input_file
import tracemalloc
import datetime


class TaskTest7(unittest.TestCase):

    def test_stack(self):
        """Тест стека"""
        # given
        lst, n, m = read_input_file()
        max_allowed_time = datetime.timedelta(seconds=2)  # Задаю ограничение по времени

        # when
        tracemalloc.start()
        start_time = datetime.datetime.now()

        find_sliding_max(lst, n, m)

        finish_time = datetime.datetime.now()
        spent_time = finish_time - start_time # Итоговое время

        current, peak = tracemalloc.get_traced_memory()
        memory_used = current / 10 ** 6 # Итоговая память

        # then
        self.assertEqual(find_sliding_max(lst, n, m), [7, 7, 5, 6, 6])
        self.assertLessEqual(spent_time, max_allowed_time)
        self.assertLessEqual(memory_used, 256)


if __name__ == "__main__":
    unittest.main()