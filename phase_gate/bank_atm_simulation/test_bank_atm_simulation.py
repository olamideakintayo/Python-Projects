#test_bank_atm_simulation.py

import unittest
from unittest import TestCase
from bank_atm_simulation import transactions, withdrawal, print_transactions, main

import unittest
from bank_atm_simulation import withdrawal

class TestBankATMWithdrawal(unittest.TestCase):

    def test_valid_withdrawal(self):
        result, message = withdrawal(5000, 10000)
        self.assertTrue(result)
        self.assertEqual(message, "")

    def test_withdrawal_not_multiple_of_500_or_1000(self):
        result, message = withdrawal(550, 10000)
        self.assertFalse(result)
        self.assertEqual(message, "The Withdrawal amount must be a multiple of 500 or 1000 naira.")

    def test_withdrawal_exceeds_90_percent(self):
        result, message = withdrawal(9100, 10000)
        self.assertFalse(result)
        self.assertEqual(message, "You Cannot withdraw more than 90% of your balance.")

    def test_withdrawal_leaves_less_than_minimum_balance(self):
        result, message = withdrawal(9900, 10000)
        self.assertFalse(result)
        self.assertEqual(message, "Insufficient balance after transaction. Minimum balance of 199 naira must remain.")

    def test_negative_balance(self):
        with self.assertRaises(ValueError):
            withdrawal(1000, -500)

if __name__ == '__main__':
    unittest.main()
