from lab2.task2.src.task2 import merge_sort
from lab2 import utils
import datetime
import tracemalloc

n, lst = utils.read_file()


def test_baza(func, lst, n):
    # На данных из примера
    print("Просчитаем время и память работы сортировки")
    tracemalloc.start()  # Запускаем счётчик памяти
    start_time = datetime.datetime.now()  # Запускаем счётчик времени

    print(merge_sort(lst, 0, n - 1))

    finish_time = datetime.datetime.now()  # Измеряем время конца работы
    print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

    current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
    print(
        f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах


if __name__ == "__main__":
    test_baza(merge_sort, lst, n)
