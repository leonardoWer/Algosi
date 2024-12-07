from lab4 import utils
import unittest
from lab4.task9.src.task9 import PatientQueue, ReadPatientData
import tracemalloc
import datetime


class TaskTest9(unittest.TestCase):

    def test_queue_performance(self):
        """Тест на время и память"""
        # given
        queue = PatientQueue()
        queue_utils = ReadPatientData()
        queue_utils.read_utils_data()

        # when
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        queue, result1 = queue_utils.fill_queue(queue)

        finish_time = datetime.datetime.now()
        spent_time = finish_time - start_time # Итоговое время

        current, peak = tracemalloc.get_traced_memory()
        memory_used = current / 10 ** 6  # Итоговая память

        # then
        self.assertEqual(queue.__str__(), "4")
        self.assertEqual(result1, ["1", "2", "3"])

    def test_queue_correctly(self):
        """Тест на корректность работы очереди"""
        # given
        queue2 = PatientQueue()
        queue_utils2 = ReadPatientData()
        queue_utils2.read_utils_data("input2.txt")

        # when
        queue2, result2 = queue_utils2.fill_queue(queue2)

        # then
        self.assertEqual(queue2.__str__(), "")
        self.assertEqual(result2, ["1", "3", "2", "5", "4"])


if __name__ == "__main__":
    unittest.main()
