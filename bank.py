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

    def __init__(self, owner, balance): # This is where the owner and balance are initialized
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):  # This is where the deposit is made by adding the amount to the balance
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount): # This is where the withdraw is made by subtracting the amount from the balance and if the balance is less than the amount it will print insufficient funds
        if self.balance < amount:
            print('Insufficient funds')
        else:
            self.balance -= amount
            return self.balance
    
    def __str__(self): # This is where the owner and balance are printed
        return f'Owner: {self.owner}\nBalance: {self.balance}'


class SaveAccount(BankAccount): # This is where the SaveAccount class is created and it inherits the BankAccount class and we put the interest rate in it
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self): #here we add the intrest rate to the balance
        self.balance += self.balance * self.interest_rate
        return self.balance

    def __str__(self): # This is where the owner, balance and interest rate are printed
        return f'Owner: {self.owner}\nBalance: {self.balance}\nInterest Rate: {self.interest_rate}'
    

BankAccount1 = BankAccount('John', 100) # This is where the first 3 bank accounts are created
BankAccount2 = BankAccount('Ali', 200)
BankAccount3 = BankAccount('Saif', 300)

print(BankAccount1.owner) # This is where the owner and balance are printed so that we can see if the above code worked
print(BankAccount1.balance)
print(BankAccount2.owner)
print(BankAccount2.balance)

BankAccount1.deposit(100) # This is where the deposit and withdraw functions are tested
BankAccount2.deposit(200)

print(BankAccount1.balance) # This is where the balance is printed to see if the deposit worked
print(BankAccount2.balance)

BankAccount1.withdraw(500) # This is where the withdraw function is tested
BankAccount2.withdraw(100)

print(BankAccount1.balance) # This is where the balance is printed to see if the withdraw worked
print(BankAccount2.balance)

print(BankAccount1) # This is where the owner and balance are printed
print(BankAccount2)
print(BankAccount3)

SaveAccount1 = SaveAccount(BankAccount1.owner, BankAccount1.balance, 0.1) # This is where the first 3 SaveAccounts are created and the interest rate is put in them
SaveAccount2 = SaveAccount(BankAccount2.owner, BankAccount2.balance, 0.2)
SaveAccount3 = SaveAccount(BankAccount3.owner, BankAccount3.balance, 0.3)

print(SaveAccount1.add_interest()) # This is where the add_interest function is tested
print(SaveAccount2.add_interest())
print(SaveAccount3.add_interest())

print(SaveAccount1) # This is where the owner, balance and interest rate are printed
print(SaveAccount2)
print(SaveAccount3)