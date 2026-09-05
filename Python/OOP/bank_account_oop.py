class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def display(self):
        print("Name :", self.name)
        print("Account Balance :", self.balance)


name = input("Enter your name: ")
balance = int(input("Enter starting balance: "))

s1 = BankAccount(name, balance)

amount = int(input("Enter deposit amount: "))

s1.deposit(amount)
s1.display()
