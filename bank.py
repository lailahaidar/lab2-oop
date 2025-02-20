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
    def init (self,owner,balance=0):
    self.owner = owner
    self.balance = balance
    def deposeit(self, amount):
        self.balance += amount
    def withdraw(self,amount):
        if ampunt < self.balance:
            print("insufficient funds")
        else:
            self.b alance -= amount 
    def str (self):
        return f"owner: {self.owner},
        balance: {self,balance}"
        class SavingsAccount(BankAccount):
            def init (self, owner, balance=0, interest_rate=0.01):
                super() init (owner, balance)
                self.interest_rate =
                interest_rate
                def str (self);
                return f"owner: {self.owner},
                balance: {self.balance}, interest Rate:
                {self.interest_rate}"
account1=BankAccount("Alice")
account2=BankAccount("Bob",100)
account3=SavingsAccount("Charlie",200,0.02)

accounts = [account1, account2, account3]
for account in accounts:
    print(account)
print(accounts[2])

            