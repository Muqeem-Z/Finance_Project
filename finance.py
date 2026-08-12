class Client:
    def __init__ (self, identifier, name, contact, local, active):
        self.name = name
        self.id = identifier
        self.contact = contact
        self.location = local #there might be different rules for local and international clients (citizenship)
        self.active = active

    def change_contact (self, new_contact):
        self.contact = new_contact

    def display_info (self):
        print("--------------------------------")
        print("          CLIENT INFO")
        print("--------------------------------")
        print(f"Client name: {self.name}")
        print(f"Client identity number: {self.id}")
        print(f"Client contact: {self.contact}")
        print(f"Is client Australian? {self.location}")
        print(f"Client Active: {self.active}")
        print("--------------------------------")
        print("")

class Account:
    def __init__ (self, acc_id, acc_type, balance, owner):
        self.acc_id = acc_id
        self.acc_type = acc_type
        self.balance = balance
        self.owner = owner

    def deposit (self, amount):
        self.balance += amount

    def withdraw (self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f"Account {self.acc_id} has insufficient funds for this withdrawl. ")
    
    def display_balance (self):
        print(f"{self.acc_id}'s account balance: ${self.balance:.2f}")


client_1 = Client(1, "Ali", "ali@gmail.com", True, True)
client_2 = Client(2, "Sarah", "0412345678", False, True)
client_3 = Client(3, "John", "john@gmail.com", True, False)

account_1 = Account(1, "Savings", 1000, client_1)
account_2 = Account(2, "Checking", 500, client_2)
account_3 = Account(3, "Savings", 2000, client_3)

client_1.display_info()
client_2.display_info()

account_1.deposit(500)
account_2.deposit(200)

account_1.withdraw(300)
account_2.withdraw(100)

account_3.withdraw(5000)

account_1.display_balance()
account_2.display_balance()
account_3.display_balance()