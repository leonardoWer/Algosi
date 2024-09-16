import time

input = open(r"C:\Python\ITMO\Algosi\lab0\task3\input.txt")
output = open(r"C:\Python\ITMO\Algosi\lab0\task3\output.txt", "w")

t_start = time.perf_counter()

n = int(input.readline())

def fib(n):
    if n<=1:
        return n
    f1, f2 = 0,1
    for i in range(2,n+1):
        f1, f2 = (f2%10), (f1+f2)%10
    return f2

if (0<=n<=10**7):
    output.write(str(fib(n)%10))
    output.close()
else:
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))

print("Время работы: %s секунд" % (time.perf_counter() - t_start))