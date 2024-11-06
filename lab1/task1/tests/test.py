from lab1.task1.src.task1 import insertion_sort
import datetime
import tracemalloc
from lab1 import utils
import unittest


class TaskTest1(unittest.TestCase):

    def test_sort(self):
        """Тест на данных из примера"""
        # given
        n, lst = utils.read_file()

        # when
        print("Просчитаем время и память работы алгоритма")
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        print(insertion_sort(n, lst))

        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

        current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
        print(
            f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах

        # then
        self.assertEqual(insertion_sort(n, lst), [26, 31, 41, 41, 58, 59])


if __name__ == "__main__":
    unittest.main()
