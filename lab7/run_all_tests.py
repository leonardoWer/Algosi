""" Запускает все тесты в лабораторной """

import unittest

from lab7.task1.tests.test import TaskTest1
from lab7.task2.tests.test import TaskTest2
from lab7.task4.tests.test import TaskTest4
from lab7.task6.tests.test import TaskTest6


def create_suit():
    """ Создаёт набор тестов, который будет запускать"""
    suite = unittest.TestSuite()
    for all_test_suit in unittest.defaultTestLoader.discover("/", "test_stack.py"):
        for test_suite in all_test_suit:
            suite.addTests(test_suite)

    return suite


if __name__ == "__main__":
    unittest.main()