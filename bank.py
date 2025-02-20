class BankAccount:
    """A class to represent a bank account."""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance  # Default balance is 0 unless specified

    def deposit(self, amount):
        """Adds money to the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws money from the account if sufficient funds are available."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def __str__(self):
        """Returns a string representation of the account."""
        return f"BankAccount(owner={self.owner}, balance=${self.balance})"


# Subclass for Savings Account with Interest Rate
class SavingsAccount(BankAccount):
    """A savings account that includes an interest rate."""
    
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Applies interest to the current balance."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of ${interest:.2f} applied. New balance: ${self.balance:.2f}")

    def __str__(self):
        return f"SavingsAccount(owner={self.owner}, balance=${self.balance:.2f}, interest_rate={self.interest_rate*100}%)"


# Creating 3 bank accounts
account1 = BankAccount("Alice", 500)
account2 = BankAccount("Bob", 300)
account3 = BankAccount("Charlie", 1000)

# Creating a list to store bank accounts
accounts = [account1, account2, account3]

# Printing the accounts in the list
print("\nBank Accounts:")
for account in accounts:
    print(account)

# Creating a savings account
savings_account = SavingsAccount("David", 2000, 0.05)

# Printing savings account before applying interest
print("\nBefore Applying Interest:")
print(savings_account)

# Applying interest
savings_account.apply_interest()

# Printing savings account after applying interest
print("\nAfter Applying Interest:")
print(savings_account)
