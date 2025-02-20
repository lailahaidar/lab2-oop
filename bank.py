# Bank Account Class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance  # Now it properly uses the provided balance

    # Deposit money to the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner} deposited: ${amount}")
        else:
            print("The deposited amount must be positive")

    # Withdraw money from the account
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew: ${amount}")
        else:
            print("Invalid withdrawal amount")

    # General print function for owner and balance
    def __str__(self):
        return f"Owner: {self.owner}, Balance: ${self.balance}"


# Create 3 bank accounts
account1 = BankAccount("Aisha", 700)
account2 = BankAccount("Noura", 800)
account3 = BankAccount("Loulwa", 900)

# Create a list to store account information
accounts = [account1, account2, account3]

# Print all accounts
for acc in accounts:
    print(acc)


# Savings Account Class (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.0):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate  # Interest rate as a percentage

    # Apply interest to the balance
    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest of ${interest:.2f} applied to {self.owner}'s account")

    # Override the string representation to include interest rate
    def __str__(self):
        return f"Owner: {self.owner}, Balance: ${self.balance}, Interest Rate: {self.interest_rate}%"


# Create a Savings Account
savings_account = SavingsAccount("Mohammed", 600, 5)  # 5% interest rate
print(savings_account)

# Apply interest
savings_account.apply_interest()
print(savings_account)
