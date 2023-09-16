'''Implement a class called bank account that represent a bank account.the class should have private
Attributes for account number,account holder name, and account balance.includes methods to
Deposit money, withdraw money, and display the account balance.ensures the account balance
Cannot be accessed directly from outside the class. Write a program to create an instance of the 
Bankaccount class and test the deposit and withdrawal functionality.'''


class Bankaccount:

   def __init__(self, account_number, account_holder_name,initial_balance=0.0):
     self.__account_number = account_number 
     self.__account_holder_name = account_holder_name
     self.__account_balance = initial_balance

   def deposit(self, amount):
     if amount > 0:
       self.__account_balance += amount
       #self.__account_balance = self.account_balance+amount 
       print("Deposited ₹{}. New balance: ₹{}".format(amount,
            self.__account_balance))
     else:
       print("invalid deposit amount.") 

   def withdrawal(self, amount): 
     if amount > 0 and amount <= self.__account_balance:
       self.__account_balance -= amount
       #self.account_balance = self.account_balance-amount 
       print("withdrew ₹{}. New balance: ₹{}".format(amount,
            self.__account_balance))
     else:
       print("invalid withdrawal amount or insufficient balance.")

   def display_balance(self):
     print("account balance for {} (account #{}): ₹{}".format(
        self.__account_holder_name, self.__account_number,
        self.__account_balance))


#create an instance of a BankAccount class 
account = Bankaccount(account_number="123456789",
         account_holder_name="Hari Prabhu",
         initial_balance=5000.0)

# test deposit and withdrawal functionality
account.display_balance()
account.deposit(500.0)
account.withdrawal(200.0)
account.withdrawal(20000.0)
account.display_balance()