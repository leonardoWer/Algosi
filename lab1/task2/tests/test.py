from operator import index

from lab1.task2.src.task2 import insertion_sort
import datetime
import tracemalloc
from lab1 import utils
import unittest


class TaskTest2(unittest.TestCase):

    def test_sort(self):
        """Тест на данных из примера"""
        # given
        n, lst = utils.read_file()

        # when
        print("Просчитаем время и память работы алгоритма")
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        indexes, res = (insertion_sort(n, lst))
        print(indexes, res)

        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

        current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
        print(
            f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах

        # then
        self.assertEqual((indexes, res), ("1 2 2 2 3 5 5 6 9 1 " , [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) )


if __name__ == "__main__":
    unittest.main()

