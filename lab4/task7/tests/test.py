from lab4 import utils
import unittest
from lab4.task7.src.task7 import find_sliding_max, read_input_file
import tracemalloc
import datetime


class TaskTest7(unittest.TestCase):

    def test_stack(self):
        """Тест стека"""
        # given
        lst, n, m = read_input_file()

        # when
        print(f"Просчитаем время и память работы stack")
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        print(find_sliding_max(lst, n, m))

        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

        current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
        print(
            f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах

        # then
        self.assertEqual(find_sliding_max(lst, n, m), [7, 7, 5, 6, 6])


if __name__ == "__main__":
    unittest.main()