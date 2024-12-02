"""
Стек с максимумом
"""

from lab4 import utils
from lab4.task1.src.task1 import Stack, Utils
import os


CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

class StackMax(Stack):
    def max(self):
        cur_el = self.head.next
        max_el = -10**9
        while cur_el:
            max_el = max(int(cur_el.value), max_el)
            cur_el = cur_el.next

        return max_el

class UtilsMax(Utils):

    def read_stack_data(self, input_file_name = "input.txt"):
        """Считывает данные для стека"""
        with open(os.path.join(CURRENT_SCRIPT_DIR_PATH, "../txtfiles/", input_file_name), "r") as file:
            self.commands_cnt = int(file.readline())
            for i in range(self.commands_cnt):
                self.commands_list.append(file.readline().strip())

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
    result = []

    my_stack1 = StackMax()  # Создаём стек
    stack_utils1 = UtilsMax()  # Создаём утилс для считывания из файла
    stack_utils1.read_stack_data()  # Считываем данные из файла
    my_stack1, result1 = stack_utils1.fill_stack(my_stack1)  # Заполняем стек и получаем список с максимальными элементами

    my_stack2 = StackMax()  # Создаём стек
    stack_utils2 = UtilsMax()  # Создаём утилс для считывания из файла
    stack_utils2.read_stack_data("input2.txt")  # Считываем данные из файла
    my_stack2, result2 = stack_utils2.fill_stack(my_stack2)  # Заполняем стек и получаем список с максимальными элементами

    my_stack3 = StackMax()  # Создаём стек
    stack_utils3 = UtilsMax()  # Создаём утилс для считывания из файла
    stack_utils3.read_stack_data("input3.txt")  # Считываем данные из файла
    my_stack3, result3 = stack_utils3.fill_stack(my_stack3)  # Заполняем стек и получаем список с максимальными элементами

    utils.write_file(CURRENT_SCRIPT_DIR_PATH, ["input 1:", result1, "\ninput 2:", result2, "\ninput 3:", result3])


