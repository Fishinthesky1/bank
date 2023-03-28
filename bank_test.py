from bank import Bank, Account, SavingsAccount, CurrentAccount

def test_open_account():
    bank = Bank()
    account = Account('John', 1000)
    bank.add_account(account)
    assert bank.get_balance(account) == 1000

def test_add_account():
    bank = Bank()
    account = SavingsAccount('Mary', 500, 0.1)
    bank.add_account(account)
    assert bank.get_balance(account) == 500

def test_update_accounts():
    bank = Bank()
    account = CurrentAccount('Peter', 1000, 500)
    bank.add_account(account)
    assert bank.get_balance(account) == 1000
    account.withdraw(1500)
    bank.update_accounts()
    # Check if overdraft letter was printed
    assert account.overdraft_letter_sent == True
