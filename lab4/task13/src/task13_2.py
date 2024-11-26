"""Очередь на основе связанного списка"""

from lab4 import utils


class Node:
    """Содержит текущий элемент и ссылку на следующий"""
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    """Очередь на основе связанного списка"""
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def __str__(self):
        result = ""
        if not self.is_empty():
            cur_el = self.head.next
            result += str(self.head.value) + ","
            while cur_el:
                result += str(cur_el.value) + ","
                cur_el = cur_el.next

        return result[:-1]

    def is_empty(self):
        """Проверка на опустошение очереди"""
        return self._length == 0

    def length(self):
        """Возвращает длину очереди"""
        return self._length

    def top(self):
        """
        Проверка на пустую очередь
         - Возвращает верхний элемент, если он есть
        """
        if self.is_empty():
            raise Exception("В пустой очереди нет верхнего элемента!")

        return self.head.value

    def enqueue(self, element):
        """Включение элемента в очередь"""
        node = Node(element)
        if self.tail is None: # Если очередь пуста, голова и хвост совпадают
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self._length += 1

    def dequeue(self):
        """Исключение первого элемента из очереди"""
        if self.is_empty():
            raise Exception("Нельзя исключить элемент из пустой очереди!")
        else:
            dequeued_element = self.head.value # Исключаем элемент из головы
            self.head = self.head.next
            if self.head is None: # Если голова осталась пустая, хвост тоже
                self.tail = None

            self._length -= 1
            return dequeued_element


if __name__ == "__main__":
    queue = Queue()
    print(queue.is_empty())

    for i in [4,8,15,16,23,42]:
        queue.enqueue(i)

    print(queue)
    print(queue.is_empty())
    print(queue.top())

    for i in range(queue.length()):
        queue.dequeue()

    print(queue)
    print(queue.is_empty())
    print(queue.top())