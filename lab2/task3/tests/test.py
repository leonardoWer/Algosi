from lab2.task3.src.task3 import find_inverse
from lab2 import utils
import datetime
import tracemalloc
import unittest


class TaskTest3(unittest.TestCase):

    def test_sort(self):
        """Тест на данных из примера"""
        # given
        n, lst = utils.read_file()

        # when
        print("Просчитаем время и память работы алгоритма")
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        print(find_inverse(n, lst))

        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

        current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
        print(
            f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах

        # then
        self.assertEqual(find_inverse(n, lst), "0")



if __name__ == "__main__":
    unittest.main()
