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

        # when
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        for i in [4, 8, 15, 16, 23, 42]:
            queue.enqueue(i)

        for i in range(2):
            queue.dequeue()

        finish_time = datetime.datetime.now()
        spent_time = finish_time - start_time  # Итоговое время

        current, peak = tracemalloc.get_traced_memory()
        memory_used = current / 10 ** 6

        # then
        self.assertEqual(queue.__str__(),"15,16,23,42")

    def test_queue_correctly(self):
        """Тест на корректность работы"""
        # given
        queue = Queue()
        empty_queue = Queue()

        # when
        for i in [4, 8, 15, 16, 23, 42]:
            queue.enqueue(i)
        for i in range(2):
            queue.dequeue()

        # then
        self.assertEqual(empty_queue.__str__(), "")

    def test_stack_is_empty(self):
        """Тест на пустоту очереди"""
        # given
        queue = Queue()
        empty_queue = Queue()

        # when
        for i in [4, 8, 15, 16, 23, 42]:
            queue.enqueue(i)
        for i in range(2):
            queue.dequeue()

        # then
        self.assertEqual(queue.is_empty(), False)
        self.assertEqual(empty_queue.is_empty(), True)

    def test_stack_length(self):
        """Тест на длину очереди"""
        # given
        queue = Queue()
        empty_queue = Queue()

        # when
        for i in [4, 8, 15, 16, 23, 42]:
            queue.enqueue(i)
        for i in range(2):
            queue.dequeue()

        # then
        self.assertEqual(queue.length(), 4)
        self.assertEqual(empty_queue.length(), 0)


if __name__ == "__main__":
    unittest.main()
