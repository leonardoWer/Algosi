from lab2.task5.src.task5 import find_el_bolsh
import datetime
import tracemalloc

file_in = open("../txtfiles/input.txt")

n = int(file_in.readline()) #Количество элементов
lst = list(map(int, file_in.readline().split())) #Список с элементами


tracemalloc.start() # Запускаем счётчик памяти
start_time = datetime.datetime.now() # Запускаем счётчик времени

print(find_el_bolsh(lst, n)) # Выводим результат отработанной функции

finish_time = datetime.datetime.now() # Измеряем время конца работы
print("Итоговое время:",finish_time - start_time) # Выводим итоговое время

current, peak = tracemalloc.get_traced_memory() # Присваеваем двум переменным память, используемую сейчас, и на пике
print(f"Используемая память: {current / 10**6} МБ\nПамять на пике: {peak / 10**6} МБ") #Выводим время работы в мегабайтах

