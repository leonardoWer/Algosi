from lab4 import utils
import unittest
from lab4.task9.src.task9 import PatientQueue, ReadPatientData
import tracemalloc
import datetime


class TaskTest9(unittest.TestCase):

    def test_queue(self):
        """Тест очереди"""
        # given
        # На примере 1
        queue = PatientQueue()
        queue_utils = ReadPatientData()
        queue_utils.read_utils_data()

        # На примере 2
        queue2 = PatientQueue()
        queue_utils2 = ReadPatientData()
        queue_utils2.read_utils_data("input2.txt")

        # when
        # На примере
        print(f"Просчитаем время и память работы stack")
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        queue, result1 = queue_utils.fill_queue(queue)

        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

        current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
        print(
            f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах

        # Остальные случаи
        queue2, result2 = queue_utils2.fill_queue(queue2)

        # then
        # На примере
        self.assertEqual(queue.__str__(),"4" )
        self.assertEqual(result1, ["1", "2", "3"])

        # Остальные случаи
        self.assertEqual(queue2.__str__(), "")
        self.assertEqual(result2, ["1", "3", "2", "5", "4"])


if __name__ == "__main__":
    unittest.main()