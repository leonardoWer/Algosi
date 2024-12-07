from lab4 import utils
import unittest
from lab4.task5.src.task5 import StackMax, UtilsMax
import tracemalloc
import datetime


class TaskTest5(unittest.TestCase):

    def test_stack_performance(self):
        """Тест на время и память"""
        # given
        my_stack = StackMax()
        stack_utils = UtilsMax()
        stack_utils.read_stack_data()
        max_allowed_time = datetime.timedelta(seconds=5) # Задаю ограничение по времени

        # when
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        my_stack, result = stack_utils.fill_stack(my_stack)  # Заполняем стек и получаем список с максимальными элементами

        finish_time = datetime.datetime.now()
        spent_time = finish_time - start_time # Затраченное время

        current, peak = tracemalloc.get_traced_memory()
        memory_used = current / 10 ** 6 # Затраченная память

        # then
        self.assertEqual(my_stack.__str__(), "2")
        self.assertEqual(result, [2, 2])
        self.assertLessEqual(spent_time, max_allowed_time)
        self.assertLessEqual(memory_used, 256)


    def test_stack_correctly(self):
        """Тест на корректность работы стека"""
        # given
        my_stack2 = StackMax()
        stack_utils2 = UtilsMax()
        stack_utils2.read_stack_data("input2.txt")

        my_stack3 = StackMax()
        stack_utils3 = UtilsMax()
        stack_utils3.read_stack_data("input3.txt")

        # when
        my_stack2, result2 = stack_utils2.fill_stack(my_stack2)
        my_stack3, result3 = stack_utils3.fill_stack(my_stack3)

        # then
        self.assertEqual(my_stack2.__str__(), "1")
        self.assertEqual(result2, [2, 1])
        self.assertEqual(my_stack3.__str__(), "1")
        self.assertEqual(result3, [])


    def test_stack_is_empty(self):
        """Тест на пустоту стека"""
        # given
        my_stack2 = StackMax()
        stack_utils2 = UtilsMax()
        stack_utils2.read_stack_data("input2.txt")

        my_stack3 = StackMax()
        stack_utils3 = UtilsMax()
        stack_utils3.read_stack_data("input3.txt")

        # when
        my_stack2, result2 = stack_utils2.fill_stack(my_stack2)
        my_stack3, result3 = stack_utils3.fill_stack(my_stack3)

        # then
        self.assertEqual(my_stack2.is_empty(), False)
        self.assertEqual(my_stack3.is_empty(), False)

    def test_stack_size(self):
        """Тест на размер стека"""
        # given
        my_stack2 = StackMax()
        stack_utils2 = UtilsMax()
        stack_utils2.read_stack_data("input2.txt")

        my_stack3 = StackMax()
        stack_utils3 = UtilsMax()
        stack_utils3.read_stack_data("input3.txt")

        # when
        my_stack2, result2 = stack_utils2.fill_stack(my_stack2)
        my_stack3, result3 = stack_utils3.fill_stack(my_stack3)

        # then
        self.assertEqual(my_stack2.size, 1)
        self.assertEqual(my_stack3.size, 1)


    def test_stack_top(self):
        """Тест на верхний элемент стека"""
        # given
        my_stack2 = StackMax()
        stack_utils2 = UtilsMax()
        stack_utils2.read_stack_data("input2.txt")

        # when
        my_stack2, result2 = stack_utils2.fill_stack(my_stack2)

        # then
        self.assertEqual(my_stack2.top(), "1")


if __name__ == "__main__":
    unittest.main()