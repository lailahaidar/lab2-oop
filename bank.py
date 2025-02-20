#Bank Account Class stores owner and balance #balance always starts at 0
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0  
#deposit money to the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")
#withdraw money from the account
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

#general print function owner and balance

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"BankAccount(owner: {self.owner}, balance: {self.balance})"

class SavingsAccount(BankAccount):
    def __init__(self, owner, interest_rate):
        super().__init__(owner)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Added {interest} interest. New balance is {self.balance}.")

    def __str__(self):
        return f"SavingsAccount(owner: {self.owner}, balance: {self.balance}, interest_rate: {self.interest_rate}%)"

# Create 3 BankAccount objects
account1 = BankAccount("Alice")
account2 = BankAccount("Bob")
account3 = BankAccount("Charlie")

# Create a list to store bank accounts
accounts = [account1, account2, account3]

# Add some transactions
account1.deposit(100)
account2.deposit(200)
account3.deposit(300)

# Print all accounts in the list
print("\nBank Accounts:")
for account in accounts:
    print(account)

# Create a SavingsAccount object with an interest rate
savings_account = SavingsAccount("Diana", 5)  # 5% interest rate
savings_account.deposit(1000)

# Add interest to the savings account
savings_account.add_interest()

# Print the SavingsAccount
print("\nSavings Account:")
print(savings_account)
