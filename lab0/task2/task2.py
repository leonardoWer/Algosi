import time

input = open(r"C:\Python\ITMO\Algosi\lab0\task2\input.txt")
output = open(r"C:\Python\ITMO\Algosi\lab0\task2\output.txt", "w")

t_start = time.perf_counter()

n = int(input.readline())
if (0<=n<=45):
    fib = [0,1]
    for i in range(2,46):
        fib.append(fib[i-2]+fib[i-1])

    output.write(str(fib[n]))
    output.close()
else:
    print("Введённый элемент не должен превышать 45")

print("Время работы: %s секунд" % (time.perf_counter() - t_start))