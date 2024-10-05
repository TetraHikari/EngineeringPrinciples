import persistent
from abc import ABC, abstractmethod
from datetime import datetime

class Customer(persistent.Persistent):
    def __init__(self, name = ""):
        self.name = name
        self.accounts = persistent.list.PersistentList()

    def __str__(self):
        return "Customer Name: " + self.name
    
    def setName(self, name):
        self.name = name

    def addAccount(self, account):
        self.accounts.append(account)
        return account
    
    def getAccounts(self, n):
        if 0 <= n < len(self.accounts):
            return self.accounts[n]
        return None
    
    def printStatus(self):
        print(self.__str__())
        for a in self.accounts:
            print("", end="     ")
            a.printStatus()


class BackTransaction(persistent.Persistent):
    def __init__(self, amount, oldBalance, newBalance, time, ttype):
        self.Amount = amount
        self.OldBalance = oldBalance
        self.NewBalance = newBalance
        self.Timestamp = time
        self.Type = ttype

    def printDetail(self):
        print("Transaction Type: " + self.Type + "\n\tAmount: " + str(self.Amount) + "\n\tOld Balance: " + str(self.OldBalance) + "\n\tNew Balance: " + str(self.NewBalance) + "\n\tTimestamp: " + str(self.Timestamp))


class Account(ABC):
    def __init__(self, balance = 0.0, owner = None):
        self.Balance = balance
        self.Owner = owner
        self.BankTransaction = persistent.list.PersistentList()

    def printBankTransaction(self):
        for b in self.BankTransaction:
            b.printDetail()

    @abstractmethod
    def __str__(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
    @abstractmethod
    def deposit(self, amount):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def withdraw(self, amount):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def transfer(self, amount, toAccount):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def transferIn(self, amount, fromAccount):
        raise NotImplementedError("Subclass must implement abstract method")  

    @abstractmethod
    def accountDetails(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
    @abstractmethod
    def getBalance(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
    @abstractmethod
    def printStatus(self):
        raise NotImplementedError("Subclass must implement abstract method")


class SavingsAccount(Account, persistent.Persistent):
    def __init__(self, balance = 0.0, owner = None, interest = 0.0):
        super().__init__(balance, owner)
        self.InterestRate = interest

    def __str__(self):
        return "Savings Account"
    
    def deposit(self, amount):
        self.Balance += amount
        self.BankTransaction.append(BackTransaction(amount, self.Balance - amount, self.Balance, datetime.now(), "Deposit"), )
    
    def withdraw(self, amount):
        if self.Balance > amount:
            self.Balance -= amount
            self.BankTransaction.append(BackTransaction(amount, self.Balance + amount, self.Balance, datetime.now(), "Withdraw"))
        else:
            print("Insufficient Funds")
    
    def transfer(self, amount, toAccount):
        if self.Balance > amount:
            self.Balance -= amount
            toAccount.deposit(amount)
            self.BankTransaction.append(BackTransaction(amount, self.Balance + amount, self.Balance, datetime.now(), "Transfer to " + str(toAccount.Owner.name)))
        else:
            print("Insufficient Funds")

    # receive money amount from account fromAccount
    def transferIn(self, amount, fromAccount):
        if fromAccount.getBalance() > amount:
            fromAccount.withdraw(amount)
            self.deposit(amount)
            self.BankTransaction.append(BackTransaction(amount, self.Balance - amount, self.Balance, datetime.now(), "Transfer from " + str(fromAccount.Owner.name)))
        else:
            print("Insufficient Funds")

    def accountDetails(self):
        return "Account Type: " + self.__str__() + "\tBalance: " + str(self.Balance) + "\tInterest Rate: " + str(self.InterestRate)
    
    def getBalance(self):
        return self.Balance
    
    def printStatus(self):
        print(self.accountDetails())
    
class CurrentAccount(Account, persistent.Persistent):
    def __init__(self, balance = 0.0, owner = None, limit = 0.0):
        super().__init__(balance, owner)
        self.OverdraftLimit = limit

    def __str__(self):
        return "Current Account"
    
    def deposit(self, amount):
        self.Balance += amount
        self.BankTransaction.append(BackTransaction(amount, self.Balance - amount, self.Balance, datetime.now(), "Deposit"))

    def withdraw(self, amount):
        if self.Balance + self.OverdraftLimit > amount:
            self.Balance -= amount
            self.BankTransaction.append(BackTransaction(amount, self.Balance + amount, self.Balance, datetime.now(), "Withdraw"))
            print("Insufficient Funds")
    
    def transfer(self, amount, toAccount):
        if self.Balance > amount:
            self.Balance -= amount
            toAccount.deposit(amount)
            self.BankTransaction.append(BackTransaction(amount, self.Balance + amount, self.Balance, datetime.now(), "Transfer to " + str(toAccount.Owner.name)))
        else:
            print("Insufficient Funds")

    # receive money amount from account fromAccount
    def transferIn(self, amount, fromAccount):
        if fromAccount.getBalance() > amount:
            fromAccount.withdraw(amount)
            self.deposit(amount)
            self.BankTransaction.append(BackTransaction(amount, self.Balance - amount, self.Balance, datetime.now(), "Transfer from " + str(fromAccount.Owner.name)))
        else:
            print("Insufficient Funds")

    def accountDetails(self):
        return "Account Type: " + self.__str__() + "\tBalance: " + str(self.Balance) + "\tOverdraft Limit: -" + str(self.OverdraftLimit)
    
    def getBalance(self):
        return self.Balance
    
    def printStatus(self):
        print(self.accountDetails())