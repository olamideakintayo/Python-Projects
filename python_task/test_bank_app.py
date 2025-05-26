# test_bank_app.py

import unittest
from unittest import TestCase
from bank_app import accounts, create_account, deposit, withdraw, get_all_accounts, find_account_by_phone

class TestBankApp(TestCase):
    def setUp(self):
        accounts.clear()

    def test_that_a_creates_single_account(self):
        create_account("Olamide", "09032592825", "5000")
        self.assertEqual(len(accounts), 1)
        self.assertEqual(accounts[0]["name"], "Olamide")
        self.assertEqual(accounts[0]["phone"], "09032592825")
        self.assertEqual(accounts[0]["balance"], 5000.0)

    def test_that_create_multiple_accounts(self):
        create_account("Olamide", "09032592825", "5000")
        create_account("Mide", "08123456789", "7500")
        create_account("Kash", "09032456789", "100000")
        self.assertEqual(len(accounts), 3)
        self.assertEqual(accounts[1]["name"], "Mide")
        self.assertEqual(accounts[1]["balance"], 7500.0)
        self.assertEqual(accounts[2]["balance"], 100000.0)

    def test_that_confirms_balance_is_float(self):
        create_account("ola", "000", "1234.56")
        self.assertIsInstance(accounts[0]["balance"], float)

    def test_that_checks_empty_account(self):
        create_account("", "", "0")
        self.assertEqual(accounts[0]["name"], "")
        self.assertEqual(accounts[0]["phone"], "")
        self.assertEqual(accounts[0]["balance"], 0.0)	

    def test_that_check_for_negative_balance(self):
        with self.assertRaises(ValueError):
            create_account("Olamide", "09032592825", "-100")

    def test_that_checks_for_non_numeric_balance(self):
        with self.assertRaises(ValueError):
            create_account("Olamide", "09032592825", "ola")


    def test_that_checks_if_deposit_increases__the_balance(self):
        create_account("Olamide", "09032592825", "1000")
        new_balance = deposit("09032592825", "500")
        self.assertEqual(new_balance, 1500.0)
        self.assertEqual(accounts[0]["balance"], 1500.0)

    def test_that_checks_if_deposit_with_negative_amount_raises_ValueError(self):
        create_account("Olamide", "09032592825", "1000")
        with self.assertRaises(ValueError):
            deposit("09032592825", "-500")

    def test_that_checks_if_deposit_with_zero_amount_raises_ValueError(self):
        create_account("Olamide", "09032592825", "1000")
        with self.assertRaises(ValueError):
            deposit("09032592825", "0")

    def test_that_checks_if_deposit_to_nonexistent_account_raises_ValueError(self):
        create_account("Olamide", "09032592825", "1000")
        with self.assertRaises(ValueError):
            deposit("00000000000", "100")

	
    def test_that_checks_if_the_withdraw_is_successful(self):
        create_account("Olamide", "09032592825", "1000")
        new_balance = withdraw("09032592825", "300")
        self.assertEqual(new_balance, 700.0)

    def test_that_checks_if_the_withdrawal_of_the_exact_balance_is_successful(self):
        create_account("Olamide", "09032592825", "500")
        new_balance = withdraw("09032592825", "500")
        self.assertEqual(new_balance, 0.0)

    def test_that_checks_if_withdrawal_of_negative_amount_is_possible(self):
        create_account("Olamide", "09032592825", "500")
        with self.assertRaises(ValueError):
            withdraw("09032592825", "-100")

    def test_that_checks_if_withdrawal_of_non_numeric_amount_is_allowed_when_inputed(self):
        create_account("Olamide", "09032592825", "500")
        with self.assertRaises(ValueError):
            withdraw("09032592825", "abc")

    def test_that_checks_if_withdrawal_of_more_than_balance_is_possible(self):
        create_account("Olamide", "09032592825", "400")
        with self.assertRaises(ValueError):
            withdraw("09032592825", "1000")

    def test_that_checks_if_withdrawal_is_possible_when_invalid_phonenumber_is_inputed(self):
        create_account("Olamide", "09032592825", "500")
        with self.assertRaises(ValueError):
            withdraw("08100000000", "100")	
            
          
    def test_that_get_all_accounts_and_returns_all_accounts(self):
        create_account("Jenny", "08123456789", "1000")
        create_account("Esther", "09011112222", "500")
        all_accounts = get_all_accounts()
        self.assertEqual(len(all_accounts), 2)
        self.assertEqual(all_accounts[0]["name"], "Jenny")
        self.assertEqual(all_accounts[1]["phone"], "09011112222")

    def test_that_get_all_accounts_and_returns_empty_when_no_account(self):
        self.assertEqual(get_all_accounts(), [])

    def test_that_find_account_by_phone_and_returns_correct_account(self):
        create_account("Lazo", "08000000000", "700")
        result = find_account_by_phone("08000000000")
        self.assertEqual(result["name"], "Lazo")
        self.assertEqual(result["balance"], 700.0)

    def test_that_find_account_by_phone_and_raises_error_if_not_found(self):
        create_account("Ngozi", "08000000000", "700")
        with self.assertRaises(ValueError):
            find_account_by_phone("08111111111")
            
                    
            