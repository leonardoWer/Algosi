import time

# ex1.1
# a,b = map(int, input("Введите число a и через пробел число b: ").split())
# if (-10**9<=a<=10**9) and (-10**9<=b<=10**9):
#     print(a + b)
# else:
#     print("Числа должны удовлетворять условию |a|<=10**9, |b|<=10**9")

# ex1.2
# a,b = map(int, input("Введите число a и через пробел число b: ").split())
# if (-10**9<=a<=10**9) and (-10**9<=b<=10**9):
#     print(a + b**2)
# else:
#     print("Числа должны удовлетворять условию |a|<=109, |b|<=109")


# ex1.3
# input = open(r"C:\Python\ITMO\Algosi\lab0\input.txt")
# output = open(r"C:\Python\ITMO\Algosi\lab0\output.txt", "w")

# a, b = map(int, input.readline().split())
# if (-10**9<=a<=10**9) and (-10**9<=b<=10**9):
#     output.write(str(a+b))
#     output.close()
# else:
#     print("Числа должны удовлетворять условию |a|<=109, |b|<=109")


# ex1.4
# input = open(r"C:\Python\ITMO\Algosi\lab0\input.txt")
# output = open(r"C:\Python\ITMO\Algosi\lab0\output.txt", "w")

# a, b = map(int, input.readline().split())
# if (-10**9<=a<=10**9) and (-10**9<=b<=10**9):
#     output.write(str(a+b**2))
#     output.close()
# else:
#     print("Числа должны удовлетворять условию |a|<=109, |b|<=109")


# ex2
# input = open(r"C:\Python\ITMO\Algosi\lab0\input.txt")
# output = open(r"C:\Python\ITMO\Algosi\lab0\output.txt", "w")

# t_start = time.perf_counter()

# n = int(input.readline())
# if (0<=n<=45):
#     fib = [0,1]
#     for i in range(2,46):
#         fib.append(fib[i-2]+fib[i-1])

#     output.write(str(fib[n]))
#     output.close()
# else:
#     print("Введённый элемент не должен превышать 45")

# print("Время работы: %s секунд" % (time.perf_counter() - t_start))

# ex3
input = open(r"C:\Python\ITMO\Algosi\lab0\input.txt")
output = open(r"C:\Python\ITMO\Algosi\lab0\output.txt", "w")

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

# ex4
# testtime


