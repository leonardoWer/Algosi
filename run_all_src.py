"""Запускает все src во всей лабораторной"""

import os
import importlib.util
import sys


def run_task(file_path):
    """Запускает задание по переданному пути"""
    task_name = os.path.basename(file_path).replace('.py', '')
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


def main(project_directory):
    """Запускает все задания во всех лабораторных"""
    for lab in os.listdir(project_directory):
        lab_path = os.path.join(project_directory, lab)
        if os.path.isdir(lab_path) and lab.startswith("lab"):
            print(f"--- Выполняется лабораторная: {lab} ---")
            for root, dirs, files in os.walk(lab_path):
                for file in files:
                    if file.endswith('.py') and 'src' in root:
                        file_path = os.path.join(root, file)
                        run_task(file_path)


if __name__ == "__main__":
    project_directory = '.'
    main(project_directory)
