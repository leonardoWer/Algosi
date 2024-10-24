from lab2.task6.src.task6 import max_podposl
import datetime
import tracemalloc


file_in = open("../txtfiles/gzp.txt").read().split("\n")

lst = []
price_lst = []
for s in file_in:
    date, price = s.split(";")
    date = str(date)
    price = price.replace(",", ".")
    price = float(price)
    lst.append([date, price])
    price_lst.append(price)


print("Просчитаем время и память работы алгоритма поиска максимальной п\п")
tracemalloc.start() # Запускаем счётчик памяти
start_time = datetime.datetime.now() # Запускаем счётчик времени

print(max_podposl("Газпром",lst, price_lst), "\n")

finish_time = datetime.datetime.now() # Измеряем время конца работы
print("Итоговое время:",finish_time - start_time) # Выводим итоговое время

current, peak = tracemalloc.get_traced_memory() # Присваеваем двум переменным память, используемую сейчас, и на пике
print(f"Используемая память: {current / 10**6} МБ\nПамять на пике: {peak / 10**6} МБ\n") #Выводим время работы в мегабайтах