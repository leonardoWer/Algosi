from lab1.task1.src.task1 import insertion_sort
from lab1.task6.src.task6 import bubble_sort
import datetime
import tracemalloc
import random

lst_hud = [random.randint(1, 100_000) for i in range(6_000)]
n_hud = 6_000

lst_sr = [random.randint(1, 10_000) for j in range(2_000)]
n_sr = 2_000

print("Просчитаем время и память работы Сортировки вставкой в худшем случае")
tracemalloc.start() # Запускаем счётчик памяти
start_time = datetime.datetime.now() # Запускаем счётчик времени

insertion_sort(n_hud, lst_hud)

finish_time = datetime.datetime.now() # Измеряем время конца работы
print("Итоговое время:",finish_time - start_time) # Выводим итоговое время

current, peak = tracemalloc.get_traced_memory() # Присваеваем двум переменным память, используемую сейчас, и на пике
print(f"Используемая память: {current / 10**6} МБ\nПамять на пике: {peak / 10**6} МБ\n") #Выводим время работы в мегабайтах



print("Просчитаем время и память работы Сортировки пузырьком в худшем случае")
tracemalloc.start() # Запускаем счётчик памяти
start_time = datetime.datetime.now() # Запускаем счётчик времени

bubble_sort(n_hud, lst_hud)

finish_time = datetime.datetime.now() # Измеряем время конца работы
print("Итоговое время:",finish_time - start_time) # Выводим итоговое время

current, peak = tracemalloc.get_traced_memory() # Присваеваем двум переменным память, используемую сейчас, и на пике
print(f"Используемая память: {current / 10**6} МБ\nПамять на пике: {peak / 10**6} МБ\n") #Выводим время работы в мегабайтах



print("Просчитаем время и память работы Сортировки вставкой в среднем случае")
tracemalloc.start() # Запускаем счётчик памяти
start_time = datetime.datetime.now() # Запускаем счётчик времени

insertion_sort(n_sr, lst_sr)

finish_time = datetime.datetime.now() # Измеряем время конца работы
print("Итоговое время:",finish_time - start_time) # Выводим итоговое время

current, peak = tracemalloc.get_traced_memory() # Присваеваем двум переменным память, используемую сейчас, и на пике
print(f"Используемая память: {current / 10**6} МБ\nПамять на пике: {peak / 10**6} МБ\n") #Выводим время работы в мегабайтах



print("Просчитаем время и память работы Сортировки пузырьком в среднем случае")
tracemalloc.start() # Запускаем счётчик памяти
start_time = datetime.datetime.now() # Запускаем счётчик времени

bubble_sort(n_sr, lst_sr)

finish_time = datetime.datetime.now() # Измеряем время конца работы
print("Итоговое время:",finish_time - start_time) # Выводим итоговое время

current, peak = tracemalloc.get_traced_memory() # Присваеваем двум переменным память, используемую сейчас, и на пике
print(f"Используемая память: {current / 10**6} МБ\nПамять на пике: {peak / 10**6} МБ\n") #Выводим время работы в мегабайтах

