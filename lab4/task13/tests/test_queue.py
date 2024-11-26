from lab4 import utils
import unittest
from lab4.task13.src.task13_2 import Queue
import tracemalloc
import datetime


class TaskTest13Queue(unittest.TestCase):

    def test_queue(self):
        """Тест стека на основе связанного списка"""
        # given
        queue = Queue()
        empty_queue = Queue()

        # when

        # На примере
        print(f"Просчитаем время и память работы stack")
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        for i in [4, 8, 15, 16, 23, 42]:
            queue.enqueue(i)

        for i in range(2):
            queue.dequeue()

        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

        current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
        print(
            f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах

        # then
        # На примере
        self.assertEqual(queue.__str__(),"15,16,23,42")
        self.assertEqual(queue.is_empty(), False)
        self.assertEqual(queue.length(), 4)

        self.assertEqual(empty_queue.__str__(), "")
        self.assertEqual(empty_queue.is_empty(), True)
        self.assertEqual(empty_queue.length(), 0)


if __name__ == "__main__":
    unittest.main()
