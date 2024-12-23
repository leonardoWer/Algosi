""" Запускает все тесты в лабораторной """

import unittest

from lab1.task1.tests.test import TaskTest1
from lab1.task2.tests.test import TaskTest2
from lab1.task3.tests.test import TaskTest3
from lab1.task4.tests.test import TaskTest4
from lab1.task5.tests.test import TaskTest5
from lab1.task6.tests.test import TaskTest6
from lab1.task7.tests.test import TaskTest7


def create_suit():
    """ Создаёт набор тестов, который будет запускать"""
    suite = unittest.TestSuite()
    for all_test_suit in unittest.defaultTestLoader.discover("/", "test.py"):
        for test_suite in all_test_suit:
            suite.addTests(test_suite)

    return suite


if __name__ == "__main__":
    unittest.main()
