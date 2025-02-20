#Bank Account Class stores owner and balance #balance always starts at 0
class bankacc:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0 
    
#deposit money to the account
def deposit(self, amount):
    if amount > 0:
        self.balance += amount
        return(f'The amount of: {amount} has been deposited. the new balance is: {self.balance}')
#withdraw money from the account
def withdraw(self, amount):
    if 0 < amount < self.balance:
        self.balance -= amount
        return f"The amount of: {amount} has been withdrawn. new balance is: {self.balance}"


#general print function owner and balance
def __info__(self):
    return f"The account name is: {self.owner}. and the balance is: {self.balance}"



#create 3 bank accounts
account1 = ("Ahmed, 5000")
account2 = ('Khaled, 100000')
account3 = ('Mohammed, 200')
#create a list to keep information about the accounts
accountsinfo = []

#add 3 objects of type BankAccount to the list
accountsinfo.append(account1)
accountsinfo.append(account2)
accountsinfo.append(account3)
#print the items in the list
for name in accountsinfo:
    print(accountsinfo)
#Create a savings account has all the functions af a bank account #plus an interest rate
saving = []
savingacc = ('Meteib')
class savingsacc(bankacc):
    def __init__(self, owner, intrest):
        self.owner = owner
        self.balance = 0
        self. intrest = intrest
    def applyint(self):
        intrest = self.balance * (self.intrest / 100)
        self.balance += intrest
    saving.append(savingacc)
    saving.deposit(2500)
    saving.applyint(5)
#print one account with the interest
print(saving)