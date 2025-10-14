#Abstraction = Hiding the complex reality while exposing only the necessary parts.

# Example With Banking System

from datetime import datetime


class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance # __ denote its private attribute
        self._history = []
        
    def show_balance(self):
        print(f"Account Balance: Rs.{self.__balance}")
    
    def deposit(self, amount):
        self.amount = amount
        self.__balance += self.amount
        self.transaction_history(amount, "Deposit")
        self.show_balance()
        
        
    def credit(self, amount):
        self.amount = amount
        self.__balance -= self.amount
        self.transaction_history(amount, "Credit")
        self.show_balance()
        
    def transaction_history(self, amount, type):
        self.amount = amount
        self.type = type 
        self._history.append(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} - {self.type} of Rs.{self.amount}")
           
    def show_history(self):
        print("Transaction History:")
        for transaction in self._history:
            print(transaction)    
        
            
acc1 = Account("123456789", "Ali", 10000)
print(acc1.account_holder)        
acc1.show_balance()
acc1.deposit(2000)
acc1.credit(500)
acc1.deposit(650)
acc1.deposit(3000)
acc1.credit(7000)

acc1.show_history()

        
# Outputs

# Ali
# Account Balance: Rs.10000
# Account Balance: Rs.12000
# Account Balance: Rs.11500
# Account Balance: Rs.12150
# Account Balance: Rs.15150
# Account Balance: Rs.8150
# Transaction History:
# 14-10-2025 22:57:46 - Deposit of Rs.2000--
# 14-10-2025 22:57:46 - Credit of Rs.500
# 14-10-2025 22:57:46 - Deposit of Rs.650
# 14-10-2025 22:57:46 - Deposit of Rs.3000
# 14-10-2025 22:57:46 - Credit of Rs.7000  