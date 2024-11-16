""" Запускает все тесты в лабораторной """

import unittest

from lab2.task1.tests.test import TaskTest1
from lab2.task2.tests.test import TaskTest2
from lab2.task3.tests.test import TaskTest3
from lab2.task4.tests.test import TaskTest4
from lab2.task5.tests.test import TaskTest5
from lab2.task6.tests.test import TaskTest6


def create_suit():
    """ Создаёт набор тестов, который будет запускать"""
    suite = unittest.TestSuite()
    for all_test_suit in unittest.defaultTestLoader.discover("/", "test.py"):
        for test_suite in all_test_suit:
            suite.addTests(test_suite)

    return suite


if __name__ == "__main__":
    unittest.main()
