"""Стек на основе связанного списка"""

from lab4 import utils
import os


CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

class Node:
    """Содержит текущий элемент и ссылку на следующий"""
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    """Стек на основе связанного списка"""
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur_el = self.head.next
        result = ""
        while cur_el:
            result += str(cur_el.value) + ","
            cur_el = cur_el.next

        return result[:-1]

    def is_empty(self):
        """
        Проверка стека на пустоту
         - Если стек пуст: False
         - Если нет: True
        """
        return self.size == 0

    def size(self):
        """Возвращает размер стека"""
        return self.size

    def push(self, element):
        """Добавляет элемент в стек"""
        node = Node(element) # Узел следующего элемента
        node.next = self.head.next # Указываем следующему узлу элемента следующий элемент головы
        self.head.next = node # Присваиваем нашей голове следующий элемент
        self.size += 1

    def pop(self):
        """Удаляет элемент из стека и возвращает его"""
        if self.is_empty():
            raise Exception("Нельзя удалить элемент из пустого списка!")
        else:
            remove_element = self.head.next
            self.head.next = remove_element.next
            self.size -=1

            return remove_element.value

    def top(self):
        """Возвращает последний элемент стека"""
        if self.is_empty():
            return None

        return self.head.next.value


class Utils:
    """Считывает и обрабатывает данные для стека"""
    def __init__(self):
        self.commands_list = []
        self.commands_cnt = None
        self.commands_name_list = []

    def read_stack_data(self):
        """Считывает данные для стека"""
        data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
        self.commands_cnt = int(data[0])
        self.commands_list = data[1:]

    def fill_commands_list(self):
        """Заполняет список, в котором операция добавления или исключения элемента из стека
        соответствует команде"""
        for el in self.commands_list:
            if "+" in el:
                self.commands_name_list.append(["push", el[1:]])
            if "-" in el:
                self.commands_name_list.append(["pop"])

    def fill_stack(self, stack):
        """
        Заполняет передаваемый стек элементами из файла
        Возвращает: (заполненный стек, элементы, которые были удалены)
        """
        pop_el_list = []
        for command in self.commands_name_list:
            if command[0] == "push":
                stack.push(command[-1])
            elif command[0] == "pop":
                pop_el_list.append(stack.pop())
        return stack, pop_el_list


def input_data():
    """Возвращает входные данные"""
    input_data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    return input_data


def main():
    my_stack = Stack()  # Создаём стек
    stack_utils = Utils()  # Создаём утилс для считывания из файла
    stack_utils.read_stack_data()  # Считываем данные из файла
    stack_utils.fill_commands_list()  # Переделываем операции в команды
    my_stack, result = stack_utils.fill_stack(my_stack)  # Заполняем стек и получаем список с удалёнными элементами

    return result


if __name__ == "__main__":
    result = main()
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, result)
