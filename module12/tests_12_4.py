import logging
import unittest
import rt_with_exceptions


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner1 = rt_with_exceptions.Runner('Serg', -2)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner2 = rt_with_exceptions.Runner(5)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s || %(levelname)s || %(message)s')
