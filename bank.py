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
        if amount > 0:
            self.balance += amount
            print(f"{self.owner} deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount!")

    def __str__(self):
        return f"Owner: {self.owner}, Balance: ${self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, owner, interest_rate):
        super().__init__(owner)
        self.interest_rate = interest_rate 
    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest applied: ${interest:.2f}. New balance: ${self.balance:.2f}")

    def __str__(self):
        return f"Owner: {self.owner}, Balance: ${self.balance:.2f}, Interest Rate: {self.interest_rate}%"

 
acc1 = BankAccount("ahmed")
acc2 = BankAccount("ismail")
acc3 = BankAccount("ali")

acc1.deposit(1000)
acc1.withdraw(300)
acc2.deposit(2000)
acc3.deposit(1500)
acc3.withdraw(500)

accounts_list = [acc1, acc2, acc3]
 
print("\nBank Accounts List:")
for acc in accounts_list:
    print(acc)

savings_acc = SavingsAccount("David", 4)
savings_acc.deposit(3000)
savings_acc.apply_interest()
 
print("\nSavings Account Details:")
print(savings_acc)
