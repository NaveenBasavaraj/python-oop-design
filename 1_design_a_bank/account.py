from abc import ABC, abstractmethod
from enum import Enum

class Account(ABC):
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @property
    def account_number(self):
        return self.__account_number

    def _change_balance(self, amount):  # better/clearer name for mutation
        self.__balance += amount

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(Account):
    def deposit(self, amount):
        if amount <= 0:
            print("Can deposit only amounts greater than 0")
            return self.balance
        self._change_balance(amount)
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Can withdraw only amounts greater than 0")
            return self.balance
        if amount > self.balance:
            print("Insufficient funds")
            return self.balance
        self._change_balance(-amount)
        return self.balance

class CurrentAccount(Account):
    def deposit(self, amount):
        if amount <= 0:
            print("Can deposit only amounts greater than 0")
            return self.balance
        self._change_balance(amount)
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Can withdraw only amounts greater than 0")
            return self.balance
        # Current accounts can go negative (overdraft), if you want to allow that, remove next lines
        if amount > self.balance:
            print("Insufficient funds")
            return self.balance
        self._change_balance(-amount)
        return self.balance

class AccountType(Enum):
    SAVINGS = "savings"
    CURRENT = "current"

class AccountFactory:
    @staticmethod
    def create_account(account_type, account_number, balance=0):
        if account_type == AccountType.SAVINGS:
            return SavingsAccount(account_number, balance)
        elif account_type == AccountType.CURRENT:
            return CurrentAccount(account_number, balance)
        else:
            raise ValueError(f"Unsupported account type: {account_type}")


if __name__ == "__main__":
    # Test SavingsAccount creation
    savings = AccountFactory.create_account(AccountType.SAVINGS, "SA001", 500)
    print("\nCreated Savings Account:", savings.account_number)
    print("Initial Balance:", savings.balance)

    # Test deposit with valid and invalid values
    print("\nDeposit 200 to Savings:")
    savings.deposit(200)
    print("Balance:", savings.balance)

    print("Deposit -50 (should not work):")
    savings.deposit(-50)
    print("Balance:", savings.balance)

    # Test withdraw with various scenarios
    print("\nWithdraw 100 from Savings:")
    savings.withdraw(100)
    print("Balance:", savings.balance)

    print("Withdraw -30 (should not work):")
    savings.withdraw(-30)
    print("Balance:", savings.balance)

    print("Withdraw 2000 (insufficient funds):")
    savings.withdraw(2000)
    print("Balance:", savings.balance)

    # Test CurrentAccount creation and overdraft behavior
    current = AccountFactory.create_account(AccountType.CURRENT, "CA001", 300)
    print("\nCreated Current Account:", current.account_number)
    print("Initial Balance:", current.balance)

    print("Deposit 150 to Current:")
    current.deposit(150)
    print("Balance:", current.balance)

    print("Withdraw 400 from Current (should work if no overdraft limit):")
    current.withdraw(400)
    print("Balance:", current.balance)

    print("Withdraw another 100 (may show insufficient funds depending on logic):")
    current.withdraw(100)
    print("Balance:", current.balance)