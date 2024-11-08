from lab3.task3.src.task3 import scarecrow_sort
from lab3 import utils
import datetime
import tracemalloc
import unittest


class TaskTest3(unittest.TestCase):

    # Тест функции быстрой сортировки на данных из примера
    def test_scarecrow_sort(self):
        """Тест сортировки Пугалом на данных из примера"""
        # given
        file_in = open("../txtfiles/input.txt")

        n1, k1 = map(int, file_in.readline().split())
        lst1 = list((map(int, file_in.readline().split())))

        n2, k2 = map(int, file_in.readline().split())
        lst2 = list((map(int, file_in.readline().split())))
        file_in.close()

        # when
        print("Просчитаем время и память работы алгоритма")
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        print(scarecrow_sort(n1,k1, lst1))

        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

        current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
        print(
            f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах

        # then
        self.assertEqual(scarecrow_sort(n1,k1, lst1), "NO")
        self.assertEqual(scarecrow_sort(n2, k2, lst2), "YES")


if __name__ == "__main__":
    unittest.main()
