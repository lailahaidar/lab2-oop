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
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
    
    def print_details(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, owner, interest_rate):
        super().__init__(owner)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        self.balance += self.balance * self.interest_rate / 100
    
    def print_details(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}, Interest Rate: {self.interest_rate}%")

# Create accounts
account1 = BankAccount("Alice")
account2 = BankAccount("Bob")
account3 = BankAccount("Charlie")
accounts = [account1, account2, account3]

# Perform transactions
account1.deposit(500)
account2.deposit(1000)
account3.deposit(1500)
account1.withdraw(200)
account2.withdraw(500)

# Print account details
for account in accounts:
    account.print_details()

# Create savings account
savings = SavingsAccount("David", 5)
savings.deposit(2000)
savings.apply_interest()
savings.print_details()




