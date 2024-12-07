import unittest
from lab4.task1.src.task1 import Stack, Utils
import tracemalloc
import datetime


class TaskTest1(unittest.TestCase):

    def test_stack_performance(self):
        """Тест на время и память"""
        # given
        my_stack = Stack()
        stack_utils = Utils()
        stack_utils.read_stack_data()
        max_allowed_time = datetime.timedelta(seconds=2) # Задаю ограничение по времени

        # when
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        stack_utils.fill_commands_list()  # Переделываем операции в команды
        my_stack, result = stack_utils.fill_stack(my_stack)  # Заполняем стек и получаем список с удалёнными элементами

        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        spent_time = finish_time - start_time  # Итоговое время

        current, peak = tracemalloc.get_traced_memory()
        memory_used = current / 10 ** 6

        # then
        self.assertEqual(my_stack.__str__(),"2,1" )
        self.assertLessEqual(spent_time, max_allowed_time)
        self.assertLessEqual(memory_used, 256)

    def test_stack_correctly(self):
        """Тест на корректность работы стека"""
        # given
        my_stack = Stack()
        empty_stack = Stack()

        # when
        my_stack.push(4)
        my_stack.push(8)
        my_stack.push(15)
        my_stack.push(16)

        # then
        self.assertEqual(my_stack.__str__(), "16,15,8,4")
        self.assertEqual(empty_stack.__str__(), "")

    def test_stack_is_empty(self):
        """Тест на пустоту стека"""
        # given
        my_stack = Stack()
        empty_stack = Stack()

        # when
        my_stack.push(4)
        my_stack.push(8)
        my_stack.push(15)
        my_stack.push(16)

        # then
        self.assertEqual(my_stack.is_empty(), False)
        self.assertEqual(empty_stack.is_empty(), True)

    def test_stack_size(self):
        """Тест на размер стека"""
        # given
        my_stack = Stack()
        empty_stack = Stack()

        # when
        my_stack.push(4)
        my_stack.push(8)
        my_stack.push(15)
        my_stack.push(16)

        # then
        self.assertEqual(my_stack.size, 4)
        self.assertEqual(empty_stack.size, 0)


    def test_stack_top(self):
        """Тест на верхний элемент стека"""
        # given
        my_stack = Stack()
        empty_stack = Stack()

        # when
        my_stack.push(4)
        my_stack.push(8)
        my_stack.push(15)
        my_stack.push(16)

        # then
        self.assertEqual(my_stack.top(), 16)


if __name__ == "__main__":
    unittest.main()