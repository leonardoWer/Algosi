from lab2.task4.src.task4 import bin_search
import datetime
import tracemalloc

file_in = open("../txtfiles/input.txt")

# Данные из примера
a = list(map(int, file_in.readline().split()))
b = list(map(int, file_in.readline().split()))

n = a[0]  # Количество элементов массива
a.remove(a[0])  # Массив

k = b[0]  # Количество элементов поиска
b.remove(k)  # Элементы поиска

tracemalloc.start() # Запускаем счётчик памяти
start_time = datetime.datetime.now() # Запускаем счётчик времени

print(bin_search(n, a, k, b)) # Выводим результат отработанной функции

finish_time = datetime.datetime.now() # Измеряем время конца работы
print("Итоговое время:", (finish_time - start_time)) # Выводим итоговое время

current, peak = tracemalloc.get_traced_memory() # Присваеваем двум переменным память, используемую сейчас, и на пике
print(f"Используемая память: {current / 10**6} МБ\nПамять на пике: {peak / 10**6} МБ") #Выводим время работы в мегабайтах

