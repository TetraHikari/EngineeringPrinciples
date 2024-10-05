class BankAccount:
    def __init__(self, bank_name, acc_name, acc_id, balance):
        self.bank_name = bank_name
        self.acc_name = acc_name
        self.acc_id = acc_id
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, money, person, date):
        self.balance += money
        print(f'{person} deposited {money} on {date}')

    def withdraw(self, money, person, date):
        self.balancce -= money
        print(f'{person} wihdraw {money} on {date}')

class SavingAccount(BankAccount):
    def __init__(self, bank_name, acc_name, acc_id, balance, interest_rate):
        super().__init__(bank_name, acc_name, acc_id, balance)
        self.interest_rate = interest_rate

    def get_interest_rate(self):
        return self.interest_rate
        
    def withdraw(self, money, person, date):
        if self.balance - money < 0:
            print('Cannot withdraw')
        else:
            self.balance -= money
            print(f'{person} withdraw {money} on {date}')

class OverDrawnAccount(BankAccount):
    def __init__(self, bank_name, acc_name, acc_id, balance):
        super.__init__(bank_name,acc_name,acc_id,balance)

    # can have negative balance
    def withdraw(self, money, person, date):
        self.balance -= money
        print(f'{person} withdraw {money} on {date}')

class Customer():
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def print_accounts(self):
        for account in self.accounts:
            print(account.acc_name)

    def get_total_balance(self):
        total = 0
        for account in self.accounts:
            total += account.get_balance()
        return total

    