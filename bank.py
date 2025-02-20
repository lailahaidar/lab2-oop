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

class Bank:
    def __init__(self, owner): # provide an owner's name and balance will start at zero
        self.owner = owner
        self.balance = 0
        self.account = owner + " " + "Balance =", self.balance
    
    def deposit(self, deposit): # owner can deposit an amount and it will print the amount deposited with the total amount
        if deposit > 0:
            self.balance += deposit
            print(f"Deposited {deposit}$, total amount is {self.balance}$")
    
    def withdraw(self, deposit): # owner can withdraw an amount and it will subtract the balance and show how much it subtracted with total amount
        if deposit < 0:
            self.balance -= deposit
            print(f"Withdrawn {deposit}$, total amount is {self.balance}$" )


# creating the bank accounts using the Bank class
owner_1 = Bank("Abdulrahman")
owner_2 = Bank("Abdulaziz")
owner_3 = Bank("Saad")



bank_list = [] # created an empty list

# appending all accounts to a list to keep information
bank_list.append(owner_1)
bank_list.append(owner_2)
bank_list.append(owner_3)

print(bank_list) # printed the items on the list

class Saving(Bank): # created a subclass called savings that has all info of bank class

    def __init__(self, owner, interest_rate=0.07): # involved all the functions from the bank class
        super().__init__(self, owner, balance)
        self.interest_rate = interest_rate # added an interest_rate in the function

    
    def apply_interest(self): # created a function that calculates the total balance plus the interest rate
        interest_rate = int(self.balance * self.interest_rate) # multiplying the balance times the interest

        self.balance += interest_rate # adding the total to the balance


