class BankAccount:
    def __init__(self, name, balance: float):
        self.name = name
        self.balance = balance

    def greeting(self, location, street):
        print(f"Hello! {self.name}, welcome to Wells Fargo Bank in {location}, {street}.")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. you new balance after deposit is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"You withdrew: {amount}. You new balance after withdraw is {self.balance}")

    def check_balance(self):
        return self.balance


id1 = BankAccount("Helen Wang", 24.99)
id1.greeting("Palo Alto", "University Ave")
id1.deposit(100)
id1.withdraw(100)
