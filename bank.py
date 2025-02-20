#Bank Account Class stores owner and balance #balance always starts at 0

#deposit money to the account

#withdraw money from the account

#general print function owner and balance

#create 3 bank accounts

#create a list to keep information about the accounts

#add 3 objects of type BankAccount to the list

#print the items in the list

#Create a savings account has all the functions af a bank account #plus an interest rate

#print one account with the interest



class BankAccount:
    """Represents a general bank account with basic operations."""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance  # Default to 0 if no balance is provided

    def deposit(self, amount):
        """Deposits a positive amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited. New balance: ${self.balance}")
        else:
            print("Deposit must be a positive amount.")

    def withdraw(self, amount):
        """Withdraws a positive amount from the account if sufficient funds are available."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be greater than zero.")

    def __str__(self):
        """Returns a string representation of the bank account."""
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance}"


class SavingsAccount(BankAccount):
    """Represents a savings account that includes an interest rate."""
    
    def __init__(self, account_holder, initial_balance=0, interest_rate=0.02):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Applies the interest rate to the current balance."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: ${interest:.2f}. New balance: ${self.balance:.2f}")

    def __str__(self):
        """Returns a string representation of the savings account."""
        return f"Savings Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}, Interest Rate: {self.interest_rate*100}%"


# Bank accounts for different users
alice_account = BankAccount("Alice", 500)
bob_account = BankAccount("Bob", 300)
charlie_account = BankAccount("Charlie", 1000)

# Store all accounts in a list
accounts = [alice_account, bob_account, charlie_account]

# Display all bank accounts
print("\nBank Accounts Overview:")
for account in accounts:
    print(account)

# Create a savings account for David
david_savings = SavingsAccount("David", 2000, 0.05)

# Print savings account details before applying interest
print("\nBefore Interest Application:")
print(david_savings)

# Apply interest to the savings account
david_savings.apply_interest()

# Print savings account details after applying interest
print("\nAfter Interest Application:")
print(david_savings)
