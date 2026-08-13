from Accounts import Account
from Clients import Client
from Transactions import Transaction
from Branches import Branch

# object creation

client_1 = Client(1, "Ali", "ali@gmail.com", True, True)
client_2 = Client(2, "Sarah", "0412345679", False, True)
client_3 = Client(3, "John", "john@gmail.com", True, False)

account_1 = Account(1, "Savings", 1000, "Jason")
account_2 = Account(2, "Checking", 500, "Jale")
account_3 = Account(3, "Savings", 2000, "Kale")

transaction1 = Transaction(1, "Payment", 500, "Payment for groceries")
transaction2 = Transaction(2, "Transfer", 2000, "Transfer to savings")
transaction3 = Transaction(3, "Transfer", 1600, "Transfer to friend's account")

branch1 = Branch(1, "abc Branch", "Adelaide", "0400000000")
branch2 = Branch(2, "xyz Branch", "City", "0400000001", "Open")
branch3 = Branch(3, "ijk Branch", "Mawson Lakes", "0400000002", "Open")

# Client methods

client_1.display_info()
client_2.display_info()
client_3.display_info()

print(client_3)
print(repr(client_3))

client_3.change_contact("john1@gmail.com")

print(client_3)
print(repr(client_3))

client_3.display_info()

# Account methods

print(account_1)
print(repr(account_2))

account_1.deposit(500)
account_2.deposit(200)

account_1.withdraw(300)
account_2.withdraw(100)

print(account_1)
print(repr(account_2))

account_3.withdraw(5000)

account_1.display_balance()
account_2.display_balance()
account_3.display_balance()

# Transaction methods

print(transaction3)
print(repr(transaction3))

transaction1.process()
transaction2.cancel()
transaction3.cancel()

transaction3.update_desc("Transfer to friend's savings account")

print(transaction3)
print(repr(transaction3))

print(transaction3.desc)

print(transaction1.status)
print(transaction2.status)
print(transaction3.status)

# Branch methods

print(branch1.available)
print(branch2.available)
print(branch3.available)

print(branch2)
print(repr(branch3))

branch1.open_branch()
branch3.close_branch()
branch2.change_phone("0400000003")

print(branch2)
print(repr(branch3))

print(branch1.available)
print(branch2.available)
print(branch3.available)
