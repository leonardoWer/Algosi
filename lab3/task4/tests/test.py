from lab3.task4.src.task4 import *
from lab2 import utils
import datetime
import tracemalloc
import unittest


class TaskTest4(unittest.TestCase):

    def test_sort(self):
        """Тест на данных из примера"""
        # given
        cnt_segment, cnt_dot, list_with_segments, list_with_dots = make_lottery_data("input")
        cnt_segment_2, cnt_dot_2, list_with_segments_2, list_with_dots_2 = make_lottery_data("input2")
        cnt_segment_3, cnt_dot_3, list_with_segments_3, list_with_dots_3 = make_lottery_data("input3")

        # when
        print("Просчитаем время и память работы алгоритма на данных из примера")
        tracemalloc.start()  # Запускаем счётчик памяти
        start_time = datetime.datetime.now()  # Запускаем счётчик времени

        print(lottery_find(list_with_segments, list_with_dots))

        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

        current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
        print(f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах

        # then
        res1 = lottery_find(list_with_segments, list_with_dots)
        res2 = lottery_find(list_with_segments_2, list_with_dots_2)
        res3 = lottery_find(list_with_segments_3, list_with_dots_3)

        self.assertEqual(res1, [1, 0, 0])
        self.assertEqual(res2, [0, 0, 1])
        self.assertEqual(res3, [2, 0])


if __name__ == "__main__":
    unittest.main()
