from lab2.task5.src.task5 import find_el_bolsh
from lab2 import utils
import datetime
import tracemalloc
import unittest


class TaskTest5(unittest.TestCase):

    def test_sort(self):
        """Тест на данных из примера"""
        # given
        n, lst = utils.read_file()

        # when
        print("Просчитаем время и память работы алгоритма")
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        print(find_el_bolsh(lst, n))

        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

        current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
        print(
            f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах

        # then
        self.assertEqual(find_el_bolsh(lst, n), "1")


if __name__ == "__main__":
    unittest.main()
