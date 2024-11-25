from lab4.task4.src.task4 import BracketChecker, read_file
from lab4 import utils
import unittest
import tracemalloc
import datetime


class TaskTest4(unittest.TestCase):

    def test_sort(self):
        """Тест на данных из примера"""
        # given
        bracket_checker = BracketChecker()
        lines_lst = read_file()
        first_line = utils.read_file_1_str()

        # when
        print(f"Просчитаем время и память работы bracket_checker")
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        print(bracket_checker.check(first_line))

        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

        current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
        print(
            f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах

        result = []
        for line in lines_lst:
            result.append(bracket_checker.check(line))

        # then

        self.assertEqual(result, ['Success', 'Success', 'Success', 'Success', 1, 3, 'Success', 10])


if __name__ == "__main__":
    unittest.main()
