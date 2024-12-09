class BankAccount:
    def __init__(self,name,balance = 0):
        self.balance = balance
        self.name = name

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def check_balance(self):
        print(f"the balance is: £{self.balance}")
    
    def display_info(self):
        print(f"hello {self.name} your balance is £{self.balance}")


x = BankAccount("x",100)
x.deposit(73)
x.withdraw(74)
x.check_balance()