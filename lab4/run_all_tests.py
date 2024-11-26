""" Запускает все тесты в лабораторной """

import unittest

from lab4.task1.tests.test import TaskTest1
from lab4.task4.tests.test import TaskTest4
from lab4.task5.tests.test import TaskTest5
from lab4.task7.tests.test import TaskTest7
from lab4.task9.tests.test import TaskTest9
from lab4.task13.tests.test_queue import TaskTest13Queue
from lab4.task13.tests.test_stack import TaskTest13Stack


def create_suit():
    """ Создаёт набор тестов, который будет запускать"""
    suite = unittest.TestSuite()
    for all_test_suit in unittest.defaultTestLoader.discover("/", "test*.py"):
        for test_suite in all_test_suit:
            suite.addTests(test_suite)

    return suite


if __name__ == "__main__":
    unittest.main()