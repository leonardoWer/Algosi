while True:
    a,b = map(int, input("Введите число a и через пробел число b: ").split())
    if (-10**9<=a<=10**9) and (-10**9<=b<=10**9):
        print(a + b)
        break
    else:
        print("Числа должны удовлетворять условию |a|<=10**9, |b|<=10**9")