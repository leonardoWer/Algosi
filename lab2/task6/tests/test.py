from lab2.task6.src.task6 import max_podposl
import datetime
import tracemalloc
import unittest


class TaskTest(unittest.TestCase):

    def test_sort(self):
        """Тест на данных из примера"""
        # given
        file_in = open("../txtfiles/gzp.txt")
        file = file_in.read().split("\n")
        lst = []
        price_lst = []
        for s in file:
            date, price = s.split(";")
            date = str(date)
            price = price.replace(",", ".")
            price = float(price)
            lst.append([date, price])
            price_lst.append(price)
        file_in.close()

        # when
        print("\n" + "Просчитаем время и память работы алгоритма поиска максимальной п\п")
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        max_podposl("Газпром", lst, price_lst)

        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

        current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
        print(
            f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах


if __name__ == "__main__":
    unittest.main()
