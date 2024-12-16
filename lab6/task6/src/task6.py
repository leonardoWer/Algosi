from lab6 import utils
import os

CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def is_fibonacci(num_str, fib_set):
    """
    Функция генерирует числа Фибоначчи и добавляет их в множество,
    пока длина числа не превысит заданное число цифр
    Множество обеспечивает эффективный поиск
    """
    return num_str in fib_set


def generate_fibonacci_until(max_digits=1000):
    """Функция проверяет, является ли строковое представление числа Фибоначчи."""
    fib_set = set()
    a, b = 1, 1
    fib_set.add(str(a))
    fib_set.add(str(b))

    while True:
        a, b = b, a + b
        fib_str = str(b)
        if len(fib_str) > max_digits:
            break
        fib_set.add(fib_str)

    return fib_set


def is_fib_list(lst: list):
    result = []
    fib_set = generate_fibonacci_until()
    for query in lst:
        if is_fibonacci(query, fib_set):
            result.append("Yes")
        else:
            result.append("No")

    return result


def input_data():
    data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    n, fib_numbers = int(data[0]), data[1:]
    return n, fib_numbers


def main():
    n, fib_numbers = input_data()
    result = is_fib_list(fib_numbers)
    return result


if __name__ == "__main__":
    result = main()
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, result, True)
