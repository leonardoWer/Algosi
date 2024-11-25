from lab4 import utils
import unittest
from lab4.task5.src.task5 import StackMax, UtilsMax
import tracemalloc
import datetime


class TaskTest5(unittest.TestCase):

    def test_stack(self):
        """Тест стека"""
        # given
        # На примере 1
        my_stack = StackMax() # Создаём стек
        stack_utils = UtilsMax() # Создаём утилс для считывания из файла
        stack_utils.read_stack_data()  # Считываем данные из файла

        # На примере 2
        my_stack2 = StackMax()  # Создаём стек
        stack_utils2 = UtilsMax()  # Создаём утилс для считывания из файла
        stack_utils2.read_stack_data("input2.txt")  # Считываем данные из файла

        # На примере 3
        my_stack3 = StackMax()  # Создаём стек
        stack_utils3 = UtilsMax()  # Создаём утилс для считывания из файла
        stack_utils3.read_stack_data("input3.txt")  # Считываем данные из файла

        # when

        # На примере
        print(f"Просчитаем время и память работы stack")
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        my_stack, result = stack_utils.fill_stack(my_stack)  # Заполняем стек и получаем список с максимальными элементами

        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

        current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
        print(
            f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах

        # Остальные случаи
        my_stack2, result2 = stack_utils2.fill_stack(my_stack2)
        my_stack3, result3 = stack_utils3.fill_stack(my_stack3)

        # then
        # На примере
        self.assertEqual(my_stack.__str__(),"2" )
        self.assertEqual(result, [2, 2])
        self.assertEqual(my_stack.top(), "2")
        self.assertEqual(my_stack2.size, 1)
        self.assertEqual(my_stack2.is_empty(), False)

        # Остальные случаи
        self.assertEqual(my_stack2.__str__(), "1")
        self.assertEqual(result2, [2, 1])
        self.assertEqual(my_stack2.size, 1)
        self.assertEqual(my_stack2.top(), "1")
        self.assertEqual(my_stack2.is_empty(), False)

        self.assertEqual(my_stack3.__str__(), "1")
        self.assertEqual(result3, [])
        self.assertEqual(my_stack3.is_empty(), False)
        self.assertEqual(my_stack3.size, 1)


if __name__ == "__main__":
    unittest.main()