from lab1.task1.src.task1 import insertion_sort
from lab2.task1.src.task1 import merge_sort
import datetime
import tracemalloc
import random

file_in = open("../txtfiles/input.txt")
file_out = open("../txtfiles/output.txt", "w")

n = int(file_in.readline())  # Количество элементов
lst = list(map(int, file_in.readline().split()))  # Список с элементами

# На данных из примера
def test_sort(func, lst):
    print("Просчитаем время и память работы сортировки")
    tracemalloc.start()  # Запускаем счётчик памяти
    start_time = datetime.datetime.now()  # Запускаем счётчик времени

    print(func(lst))

    finish_time = datetime.datetime.now()  # Измеряем время конца работы
    print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

    current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
    print(f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах

# test_sort(merge_sort, lst)


# На самых больших данных
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


# Сравнение сортировок на средних данных
def vs_test_middle(func1, func2):
    lst_sr = [random.randint(1, 10_000) for j in range(2_000)]
    n_sr = 2_000

    print(f"Просчитаем время и память работы Сортировки {func1} в среднем случае")
    tracemalloc.start()  # Запускаем счётчик памяти
    start_time = datetime.datetime.now()  # Запускаем счётчик времени

    func1(lst_sr)

    finish_time = datetime.datetime.now()  # Измеряем время конца работы
    print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

    current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
    print(f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах


    print(f"Просчитаем время и память работы Сортировки {func2} в среднем случае")
    tracemalloc.start()  # Запускаем счётчик памяти
    start_time = datetime.datetime.now()  # Запускаем счётчик времени

    func2(n_sr, lst_sr)

    finish_time = datetime.datetime.now()  # Измеряем время конца работы
    print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

    current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
    print(
        f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах

# vs_test_middle(merge_sort, insertion_sort)


# Сравнение сортировок на больших данных
def vs_test_hard(func1, func2):
    lst_hud = [random.randint(1, 1_000_000) for i in range(8_000)]
    n_hud = 8_000

    print(f"Просчитаем время и память работы Сортировки {func1} в худшем случае")
    tracemalloc.start()  # Запускаем счётчик памяти
    start_time = datetime.datetime.now()  # Запускаем счётчик времени

    func1(lst_hud)

    finish_time = datetime.datetime.now()  # Измеряем время конца работы
    print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

    current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
    print(f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах


    print(f"Просчитаем время и память работы Сортировки {func2} в худшем случае")
    tracemalloc.start()  # Запускаем счётчик памяти
    start_time = datetime.datetime.now()  # Запускаем счётчик времени

    func2(n_hud, lst_hud)

    finish_time = datetime.datetime.now()  # Измеряем время конца работы
    print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

    current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
    print(f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах

# vs_test_hard(merge_sort, insertion_sort)


