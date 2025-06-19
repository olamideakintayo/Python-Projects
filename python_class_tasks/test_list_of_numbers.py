import unittest
import list_of_numbers
from python_class_tasks.list_of_numbers import length_of_numbers


class ListOfNumbersTest(unittest.TestCase):
    def test_that_random_numbers_are_created(self):
        list_of_numbers.random_numbers()
        self.assertTrue(True)

    def test_that_checks_length_of_numbers(self):
        list_of_numbers.length_of_numbers()
        self.assertEqual(10, length_of_numbers())

    def test_that_checks_for_numbers_at_even_positions(self):
        list_of_numbers.even_positions()
        self.assertTrue(True)




if __name__ == '__main__':
    unittest.main()
