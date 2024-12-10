"""Запускает все файлы внутри src всей лабораторной"""

import os
import importlib.util
import sys


def run_task(file_path):
    """Запускает задание по переданному пути"""
    # Извлекаем имя файла без расширения
    task_name = os.path.basename(file_path).replace('.py', '')

    # Импортируем модуль
    spec = importlib.util.spec_from_file_location(task_name, file_path)
    task_module = importlib.util.module_from_spec(spec)
    sys.modules[task_name] = task_module
    spec.loader.exec_module(task_module)

    # Предполагаем, что в каждом файле есть функция main(), которая выполняет задание
    if hasattr(task_module, 'main'):
        input_data = task_module.input_data()  # Функция для получения входных данных
        output_data = task_module.main()  # Функция, которая возвращает результат
        print(f"\nЗадание {task_name}:")
        print(f"Входные данные: {input_data}")
        print(f"Результат: {output_data}")
    else:
        print(f"В файле {task_name} нет функции main!")


def main(lab_directory):
    """Запускает все src в лабораторной"""
    print(f"--- Выполняется {os.path.basename(os.path.dirname(__file__))} ---")
    # Проходим по всем папкам в lab_directory
    for root, dirs, files in os.walk(lab_directory):
        for file in files:
            if file.endswith('.py') and 'src' in root:
                file_path = os.path.join(root, file)
                run_task(file_path)


if __name__ == "__main__":
    lab_directory = '.'
    main(lab_directory)
