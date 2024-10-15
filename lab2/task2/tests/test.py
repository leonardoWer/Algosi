from lab2.task2.src.task2 import merge_sort
import datetime
import tracemalloc
import random


def test_sort_hard(func):
    lst_hud = [random.randint(1, 10**9) for i in range(10**5)]

    print(f"Просчитаем время и память работы Сортировки {func} в худшем случае")
    tracemalloc.start()  # Запускаем счётчик памяти
    start_time = datetime.datetime.now()  # Запускаем счётчик времени

    func(lst_hud)

    finish_time = datetime.datetime.now()  # Измеряем время конца работы
    print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

    current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
    print(f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах

test_sort_hard(merge_sort)