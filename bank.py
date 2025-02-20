#Bank Account Class stores owner and balance #balance always starts at 0
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

#deposit money to the account
    def deposit(self):
        deposit = int(input("how many you want to add: "))
        self.balance +=deposit
        print(f"Added {deposit} to the balance")
        print("available balance: ",self.balance)

#withdraw money from the account
    def withdraw(self):
        withdraww = int(input("what do you want to withdraw: "))
        self.balance -= withdraww
        if withdraww <= self.balance:
            self.balance -= withdraww
            print(f"Subtracted {withdraww} from the balance")
        else:
            print("Insufficient funds")
        print("available balance: ", self.balance)
#general print function owner and balance
    def __str__(self):
        return f"owner: {self.owner}, balaance: {self.balance}"
#create 3 bank accounts

BankAccount1 = BankAccount("aysha", 100)
banlaccount2 = BankAccount("abdulrahman", 200)
BankAccount3 = BankAccount("alia", 300)

#create a list to keep information about the accounts
accounts = []
#add 3 objects of type BankAccount to the list
accounts.append(BankAccount1)
accounts.append(banlaccount2)
accounts.append(BankAccount3)
BankAccount1.deposit()
BankAccount1.withdraw()

#print the items in the list
for account in accounts:
    print(account)
#Create a savings account has all the functions af a bank account #plus an interest rate
class Saving(BankAccount):
         def __init__(self,owner,balance):
          super().__init__(owner,balance)
         def saving_money(self):
             saving = self.balance * 0.2
             return saving
    
             
             

#print one account with the interest
savings_account = Saving("aysha",55)
print(f"your saving is: {savings_account.saving_money()}")
