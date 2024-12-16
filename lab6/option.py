"""Функция для нахождения номеров задач, обязательных для выполнения"""


def find_option() -> (int, int):
    v = 15
    a = 40
    p = 29
    family = "Левахин"
    b = 0
    for s in family:
        b += ord(s)

    first_task = (a * v % p) % 9
    second_task = ((a * v + b) % p) % 9

    return first_task, second_task


def main():
    first_task, second_task = find_option()
    print(f"Первой нужно выполнить задачу {first_task}, а второй {second_task}")


if __name__ == "__main__":
    main()
