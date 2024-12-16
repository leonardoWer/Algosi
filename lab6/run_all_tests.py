""" Запускает все тесты в лабораторной """

import unittest

from lab6.task2.tests.test import TaskTest2
from lab6.task3.tests.test import TaskTest3
from lab6.task5.tests.test import TaskTest5
from lab6.task6.tests.test import TaskTest6
from lab6.task8.tests.test import TaskTest8


def create_suit():
    """ Создаёт набор тестов, который будет запускать"""
    suite = unittest.TestSuite()
    for all_test_suit in unittest.defaultTestLoader.discover("/", "test_stack.py"):
        for test_suite in all_test_suit:
            suite.addTests(test_suite)

    return suite


if __name__ == "__main__":
    unittest.main()