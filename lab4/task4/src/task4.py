"""
Скобочная последовательность. Версия 2
"""

from lab4 import utils


class BracketChecker:
    """Проверяет, нет ли ошибок в скобочной последовательности"""

    def __init__(self):
        # Словарь для соответствия открывающих и закрывающих скобок
        self.pairs = {'(': ')', '[': ']', '{': '}'}

    def check(self, row):
        """
        Проверяет на отсутствие закрывающих и открывающих скобок
         - Если таких нет: Success
         - Если есть: Выводит индекс такой (начиная с 1)
        """
        stack = []
        index_stack = []

        for index, char in enumerate(row):
            if char in self.pairs: # Для открывающей скобки
                stack.append(char)
                index_stack.append(index + 1)

            elif char in self.pairs.values(): # Для закрывающей скобки
                # Проверяем, есть ли соответствующая открывающая скобка
                if stack and self.pairs[stack[-1]] == char:
                    stack.pop()  # Убираем соответствующую открывающую скобку
                    index_stack.pop()  # Убираем соответствующий индекс
                else:
                    return index + 1  # Возвращаем индекс закрывающей скобки

        if index_stack:
            return index_stack[0]  # Возвращаем индекс первой открывающей скобки без закрывающей

        return "Success"


def read_file() -> list:
    """Считывает все строки из файла"""
    with open("../txtfiles/input.txt") as file:
        lines_lst = (file.read().split("\n"))

    return lines_lst


if __name__ == "__main__":
    bracket_checker = BracketChecker()
    lines_lst = read_file()
    result = []
    for line in lines_lst:
        result.append(bracket_checker.check(line))

    utils.write_file(result)