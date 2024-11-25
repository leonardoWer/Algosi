from lab4 import utils
import unittest
from lab4.task1.src.task1 import Stack, Utils
import tracemalloc
import datetime


class TaskTest1(unittest.TestCase):

    def test_stack(self):
        """Тест стека"""
        # given

        # На примере
        my_stack = Stack() # Создаём стек
        stack_utils = Utils() # Создаём утилс для считывания из файла
        stack_utils.read_stack_data()  # Считываем данные из файла

        # Остальные случаи
        stack1 = Stack()
        stack2 = Stack()

        # when

        # На примере
        print(f"Просчитаем время и память работы stack")
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        stack_utils.fill_commands_list()  # Переделываем операции в команды
        my_stack, result = stack_utils.fill_stack(my_stack)  # Заполняем стек и получаем список с удалёнными элементами

        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

        current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
        print(
            f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах

        # Остальные случаи
        stack1.push(4)
        stack1.push(8)
        stack1.push(15)
        stack1.push(16)

        # then
        # На примере
        self.assertEqual(my_stack.__str__(),"2,1" )

        # Остальные случаи
        self.assertEqual(stack1.__str__(), "16,15,8,4")
        self.assertEqual(stack1.size, 4)
        self.assertEqual(stack1.top(), 16)
        self.assertEqual(stack1.is_empty(), False)

        self.assertEqual(stack2.__str__(), "")
        self.assertEqual(stack2.is_empty(), True)
        self.assertEqual(stack2.size, 0)


if __name__ == "__main__":
    unittest.main()