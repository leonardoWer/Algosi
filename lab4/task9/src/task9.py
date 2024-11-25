"""
Сортировка целых чисел
"""

from lab4 import utils


class PatientQueue:
    """Очередь пациентов на основе списка"""

    def __init__(self):
        self.queue = []
        self.length = 0

    def __str__(self):
        return " ".join(self.queue)

    def length(self):
        """Возвращает длину очереди"""
        return self.length

    def is_empty(self):
        """
        Проверка стека на пустоту
         - Если стек пуст: False
         - Если нет: True
        """
        return self.length == 0

    def enqueue_to_end(self, patient_number):
        """Включить элемент в очередь"""
        self.queue.append(patient_number)
        self.length += 1

    def enqueue_to_middle(self, patient_number):
        """Включить элемент в очередь"""
        middle_index = (self.length + 1)//2
        self.queue.insert(middle_index, patient_number)
        self.length += 1

    def dequeue(self):
        """Исключить первый элемент из очереди"""
        self.length -= 1
        return self.queue.pop(0)


class ReadPatientData:
    """Считывает и обрабатывает данные для очереди пациентов"""

    def __init__(self):
        self.patients_list = []
        self.commands_cnt = None

    def read_utils_data(self, input_file_name = "input.txt"):
        """Считывает данные для стека"""
        with open("../txtfiles/" + input_file_name, "r") as file:
            self.commands_cnt = int(file.readline())
            for i in range(self.commands_cnt):
                self.patients_list.append(file.readline().strip())

    def fill_queue(self, queue):
        """
        Заполняет передаваемую очередь элементами из файла
        Возвращает: заполненную очередь, список пациентов, зашедших к врачу(исключенные из очереди)
        """
        pop_patients_list = []
        for patient in self.patients_list:
            if patient[0] == "+":
                queue.enqueue_to_end(patient[1])
            elif patient[0] == "*":
                queue.enqueue_to_middle(patient[1])
            elif patient[0] == "-":
                pop_patients_list.append(queue.dequeue())

        return queue, pop_patients_list


if __name__ == "__main__":
    # Для первого инпута
    queue = PatientQueue()
    queue_utils = ReadPatientData()
    queue_utils.read_utils_data()
    queue, result1 = queue_utils.fill_queue(queue)

    # Для второго инпута
    queue2 = PatientQueue()
    queue_utils2 = ReadPatientData()
    queue_utils2.read_utils_data("input2.txt")
    queue2, result2 = queue_utils2.fill_queue(queue2)

    result = ["input1"] + result1 + ["\ninput2"] + result2
    utils.write_file(result)
