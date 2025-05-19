# test_categorize_numbers.py

import categorize_numbers  
import unittest
from unittest import TestCase


class TestCategorizeNumbers(TestCase):

    def test_divisible_numbers_present(self):
        self.assertEqual(categorize_numbers.categorize_numbers(10, 15, 21, 30, divisible_number_by=5), [10, 15, 30])

    def test_number_divisible_numbers(self):
        self.assertEqual(categorize_numbers.categorize_numbers(1, 3, 7, divisible_number_by=2), "No divisible number found")

    def test_all_numbers_divisible(self):
        self.assertEqual(categorize_numbers.categorize_numbers(6, 12, 18, divisible_number_by=6), [6, 12, 18])

    def test_empty_input(self):
        self.assertEqual(categorize_numbers.categorize_numbers(divisible_number_by=3), "No divisible number found")

    def test_default_divisor(self):
        self.assertEqual(categorize_numbers.categorize_numbers(2, 4, 5), [2, 4])    	   

    def test_with_negative_numbers(self):
        self.assertEqual(categorize_numbers.categorize_numbers(-10, -20, 5, divisible_number_by=5), [-10, -20, 5])
