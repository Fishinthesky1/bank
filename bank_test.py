import unittest
from bank import Bank, SavingsAccount, CurrentAccount

class TestBank(unittest.TestCase):
    
    def test_open_account(self):
        bank = Bank()
        account = SavingsAccount(1000, 0.5)
        bank.add_account(account)
        self.assertIn(account, bank.accounts)
        self.assertEqual(account.get_balance(), 1000)
        
    def test_update_accounts(self):
        bank = Bank()
        savings_account = SavingsAccount(1000, 0.5)
        current_account = CurrentAccount(500, -1000)
        bank.add_account(savings_account)
        bank.add_account(current_account)
        with self.assertLogs() as log:
            bank.update_accounts()
        self.assertIn("WARNING: Account overdrawn!", log.output)
        self.assertAlmostEqual(savings_account.get_balance(), 1005.0)
        self.assertAlmostEqual(current_account.get_balance(), 500.0)
