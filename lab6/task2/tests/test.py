from lab6.task2.src.task2 import *
from lab6 import utils
import unittest
import datetime
import tracemalloc


class TaskTest2(unittest.TestCase):

    def test_func_performance(self):
        """Тест функции на время и память"""
        # given
        my_phone_book = PhoneBook()
        contacts = ["add 911 police", "add 76213 Mom", "add 17239 Bob", "find 76213", "find 910", "find 911", "del 910", "del 911", "find 911", "find 76213", "add 76213 daddy", "find 76213"]

        max_allowed_time = datetime.timedelta(seconds=6)  # Задаю ограничение по времени

        # when
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        result = my_phone_book.commands_to_actions(contacts)

        finish_time = datetime.datetime.now()
        spent_time = finish_time - start_time  # Итоговое время

        current, peak = tracemalloc.get_traced_memory()
        memory_used = current / 10 ** 6

        # then
        self.assertEqual(result, ['Mom', 'not found', 'police', 'not found', 'Mom', 'daddy'])
        self.assertLessEqual(spent_time, max_allowed_time)
        self.assertLessEqual(memory_used, 512)


    def test_func_correctly(self):
        """Тест на корректность работы"""
        # given
        contacts1 = ["add 911 police", "add 76213 Mom", "add 17239 Bob", "find 76213", "find 910", "find 911", "del 910", "del 911", "find 911", "find 76213", "add 76213 daddy", "find 76213"]
        contacts2 = ["find 3839442","add 123456 me","add 0 granny","find 0","find 123456","del 0","del 0","find 0"]
        phone_book1 = PhoneBook()
        phone_book2 = PhoneBook()

        # when
        result1 = phone_book1.commands_to_actions(contacts1)
        result2 = phone_book2.commands_to_actions(contacts2)

        # then
        self.assertEqual(result1, ['Mom', 'not found', 'police', 'not found', 'Mom', 'daddy'])
        self.assertEqual(result2, ['not found', 'granny', 'me', 'not found'])


if __name__ == "__main__":
    unittest.main()
