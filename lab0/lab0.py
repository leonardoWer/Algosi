import time

# ex1.1
# a,b = map(int, input("Введите число a и через пробел число b: ").split())
# print(a + b)

# ex1.2
# a,b = map(int, input("Введите число a и через пробел число b: ").split())
# print(a + b**2)

# ex1.3
# input = open(r"C:\Python\ITMO\Algosi\lab0\input.txt")
# output = open(r"C:\Python\ITMO\Algosi\lab0\output.txt", "w")

# a, b = map(int, input.readline().split())
# output.write(str(a+b))
# output.close()

# ex1.4
# input = open(r"C:\Python\ITMO\Algosi\lab0\input.txt")
# output = open(r"C:\Python\ITMO\Algosi\lab0\output.txt", "w")

# a, b = map(int, input.readline().split())
# output.write(str(a+b**2))
# output.close()

# ex2
# input = open(r"C:\Python\ITMO\Algosi\lab0\input.txt")
# output = open(r"C:\Python\ITMO\Algosi\lab0\output.txt", "w")

# t_start = time.perf_counter()

# n = int(input.readline())

# fib = [0,1]
# for i in range(2,45):
#     fib.append(fib[i-2]+fib[i-1])

# output.write(str(fib[n]))
# output.close()

# print("Время работы: %s секунд" % (time.perf_counter() - t_start))

# ex3
# input = open(r"C:\Python\ITMO\Algosi\lab0\input.txt")
# output = open(r"C:\Python\ITMO\Algosi\lab0\output.txt", "w")

# t_start = time.perf_counter()

# n = int(input.readline())

# def fib(n):
#     if n<=1:
#         return n
#     f1, f2 = 0,1
#     for i in range(2,n+1):
#         f1, f2 = f2, f1+f2
#     return f2

# output.write(str(fib(n)%10))
# output.close()

# print("Время работы: %s секунд" % (time.perf_counter() - t_start))

# ex4
# testtime


