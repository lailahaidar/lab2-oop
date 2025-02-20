#Bank Account Class stores owner and balance #balance always starts at 0  -

#deposit money to the account  -

#withdraw money from the account  -

#general print function owner and balance -

#create 3 bank accounts  -

#create a list to keep information about the accounts  -

#add 3 objects of type BankAccount to the list  -

#print the items in the list  -

#Create a savings account has all the functions af a bank account #plus an interest rate   -

#print one account with the interest  -




class BankAccount:   
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Withdraw amount must be positive and less than or equal to the balance.")

    def __str__(self):
        return (f" Account Owner: {self.owner}, Balance: {self.balance} ")

class SavingsAccount(BankAccount):
    def __init__(self, owner, interest_rate):
        super().__init__(owner)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print( f"Applied interest: {interest}. New balance: {self.balance} ")


account1 = BankAccount(" Hamad ")
account2 = BankAccount(" Ali ")
account3 = BankAccount(" Abdullah ")


accounts = [account1, account2, account3]


account1.deposit(100)
account2.deposit(200)
account3.deposit(300)


for account in accounts:
    print(account)


savings_account = SavingsAccount(" Hamad ", 5)
savings_account.deposit(1000)
savings_account.apply_interest()


print(savings_account)