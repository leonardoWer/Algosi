input = open(r"C:\Python\ITMO\Algosi\lab0\task1\input.txt")
output = open(r"C:\Python\ITMO\Algosi\lab0\task1\output.txt", "w")

a, b = map(int, input.readline().split())
if (-10**9<=a<=10**9) and (-10**9<=b<=10**9):
    output.write(str(a+b))
    output.close()
else:
    print("Числа должны удовлетворять условию |a|<=109, |b|<=109")