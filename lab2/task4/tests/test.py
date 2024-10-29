from lab2.task4.src.task4 import bin_search
from lab2 import utils
import datetime
import tracemalloc
import unittest


class TaskTest(unittest.TestCase):

    def test_sort(self):
        """Тест на данных из примера"""
        # given
        n, a, k, b = utils.read_file_4()

        # when
        print("Просчитаем время и память работы алгоритма")
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        print(bin_search(n, a, k, b))

        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

        current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
        print(
            f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах

        # then
        self.assertEqual(bin_search(n, a, k, b), [2, 0, -1, 0, -1])


if __name__ == "__main__":
    unittest.main()
