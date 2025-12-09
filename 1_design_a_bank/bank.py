from account import AccountFactory, SavingsAccount, CurrentAccount, AccountType
from customer import Customer

class Bank:
    _instance = None  # For singleton pattern

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Bank, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'customers'):
            self.customers = dict()
        if not hasattr(self, 'accounts'):
            self.accounts = dict()
    
    def add_customer(self, customer_obj):
        self.customers[customer_obj.customer_id] = customer_obj
    
    def open_account(self, customer_id, account_type, account_number, balance=0):
        customer = self.customers.get(customer_id)
        if not customer:
            raise ValueError("Customer does not exist")
        account = AccountFactory.create_account(account_type, account_number, balance)
        customer.add_account(account)
        self.accounts[account.account_number] = account
    
    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            raise ValueError("Account not found")
        account.deposit(amount)
    
    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            raise ValueError("Account not found")
        account.withdraw(amount)
    
    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.accounts.get(from_account_number)
        to_account = self.accounts.get(to_account_number)
        if from_account is None or to_account is None:
            raise ValueError("One or both accounts not found.")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > from_account.balance:
            raise ValueError("Insufficient funds.")
        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(f"Transferred {amount} from {from_account_number} to {to_account_number}.")
        return True
    
if __name__ == "__main__":
    # Create bank instance (singleton)
    bank = Bank()

    # Create customers
    alice = Customer("Alice", "C001")
    bob = Customer("Bob", "C002")

    # Add customers to bank
    bank.add_customer(alice)
    bank.add_customer(bob)

    # Open accounts
    bank.open_account("C001", AccountType.SAVINGS, "A100", 1000)
    bank.open_account("C002", AccountType.SAVINGS, "A200", 500)

    # Transactions
    print("Alice's Savings Balance:", bank.accounts["A100"].balance)
    print("Bob's Savings Balance:", bank.accounts["A200"].balance)

    print("\n-- Deposit 200 to Bob (A200) --")
    bank.deposit("A200", 200)
    print("Bob's Savings Balance:", bank.accounts["A200"].balance)

    print("\n-- Alice to Bob Transfer 300 --")
    bank.transfer("A100", "A200", 300)
    print("Alice's Balance:", bank.accounts["A100"].balance)
    print("Bob's Balance:", bank.accounts["A200"].balance)

    print("\n-- Withdraw 100 from Alice (A100) --")
    bank.withdraw("A100", 100)
    print("Alice's Balance:", bank.accounts["A100"].balance)