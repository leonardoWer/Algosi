from lab1.task7.src.task7 import Sortland
import datetime
import tracemalloc
from lab1 import utils
import unittest


class TaskTest7(unittest.TestCase):

    def test_sort(self):
        """Тест на данных из примера"""
        # given
        file_in = open("../txtfiles/input.txt")
        n = int(file_in.readline())  # Количество элементов
        lst = list(map(float, file_in.readline().split()))  # Список с элементами
        file_in.close()

        # when
        print("Просчитаем время и память работы алгоритма")
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        print(Sortland(n, lst))

        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

        current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
        print(
            f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах

        # then
        self.assertEqual(Sortland(n, lst), [3, 4, 1])


if __name__ == "__main__":
    unittest.main()

