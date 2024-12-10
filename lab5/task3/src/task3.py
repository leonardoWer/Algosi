"""
Сортировка Пугалом
"""

from lab4 import utils
import os


CURRENT_SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def process_packets(s:int, n:int, packets_info:list) -> list:
    buffer = []  # очередь для хранения пакетов
    current_time = 0  # текущее время
    results = []

    for packet in packets_info:
        arrival_time = packet[0]
        processing_time = packet[1]

        # Удаляем обработанные пакеты из буфера
        while buffer and buffer[0] <= arrival_time:
            buffer.pop(0)

        # Проверяем, можем ли мы добавить пакет в буфер
        if len(buffer) < s:
            # Если процессор свободен, обновляем текущее время до времени прибытия пакета
            if current_time < arrival_time:
                current_time = arrival_time

            # Начинаем обработку нового пакета
            results.append(current_time)  # время начала обработки
            current_time += processing_time  # обновляем текущее время на время обработки
            buffer.append(current_time)
        else:
            results.append(-1)  # пакет отброшен

    return results


def input_data_handler(data:list[list]) -> (int, int, list):
    """
    Обрабатывает входные данные, разделяя их
    - Принимает: список со всеми данными
    - Возвращает: (s - размер буфера, n - количество пакетов, packets_info - информация о передаваемых пакетах)
    """
    s, n = data[0][0], data[0][1]
    packets_info = data[1:]
    return s, n, packets_info


def input_data():
    data = utils.read_file(CURRENT_SCRIPT_DIR_PATH)
    result = []
    for s in data:
        if s == '':
            break
        s, n = map(int, s.split())
        result.append([s, n])

    return result


def main():
    data = input_data()
    s, n, packets_info = input_data_handler(data)
    result = process_packets(s, n, packets_info)

    return result


if __name__ == "__main__":
    result = main()
    utils.write_file(CURRENT_SCRIPT_DIR_PATH, result)
