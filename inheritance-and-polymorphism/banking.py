class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount

class SavingsAccount(Account):
    def add_interest(self):
        self.balance += self.balance * 0.05   # 5% interest

s = SavingsAccount("Alex", 100000)
s.deposit(50000)
s.add_interest()
print(s.balance) 