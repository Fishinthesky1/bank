class Account:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
        
    def close_account(self):
        self.balance = 0
        
    def get_balance(self):
        return self.balance
    
class SavingsAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate
        
    def add_interest(self):
        self.balance *= (1 + self.interest_rate / 100)
        
    def is_savings_account(self):
        return True
        
class CurrentAccount(Account):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit
        
    def send_overdraft_notice(self):
        if self.balance < 0:
            print("WARNING: Account overdrawn!")
            
    def is_current_account(self):
        return True
        
class Bank:
    def __init__(self):
        self.accounts = []
        
    def add_account(self, account):
        self.accounts.append(account)
        
    def close_account(self, account):
        self.accounts.remove(account)
        
    def pay_dividends(self, rate):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.deposit(account.balance * rate / 100)
                
    def update_accounts(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                account.send_overdraft_notice()

# Створення облікових записів
savings_account = SavingsAccount(1000, 5)
current_account = CurrentAccount(500, 1000)

# Створення банку і додавання облікових записів до нього
bank = Bank()
bank.add_account(savings_account)
bank.add_account(current_account)

# Перевірка стану рахунків
print(savings_account.get_balance()) 
print(savings_account.is_savings_account())  
print(current_account.get_balance())  
print(current_account.is_current_account())  