"""
Анти-быстрая сортировка
"""

from lab4 import utils
from lab4.task1.src.task1 import Stack, Utils


class StackMax(Stack):
    def max(self):
        cur_el = self.head.next
        max_el = -10**9
        while cur_el:
            max_el = max(int(cur_el.value), max_el)
            cur_el = cur_el.next

        return max_el

class UtilsMax(Utils):

    def fill_stack(self, stack):
        max_el_list = []
        for command in self.commands_list:
            command = command.split()
            if command[0] == "push":
                stack.push(command[-1])
            elif command[0] == "pop":
                stack.pop()
            elif command[0] == "max":
                max_el_list.append(stack.max())
        return stack, max_el_list


if __name__ == "__main__":
    my_stack = StackMax()  # Создаём стек
    stack_utils = UtilsMax()  # Создаём утилс для считывания из файла
    stack_utils.read_stack_data()  # Считываем данные из файла
    my_stack, result = stack_utils.fill_stack(my_stack)  # Заполняем стек и получаем список с максимальными элементами

    print(my_stack)
    utils.write_file(result, True)


