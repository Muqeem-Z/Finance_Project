from Accounts import Account
from Clients import Client
from Transactions import Transaction
from Branches import Branch

client_1 = Client(1, "Ali", "ali@gmail.com", True, True)
client_2 = Client(2, "Sarah", "0412345679", False, True)
client_3 = Client(3, "John", "john@gmail.com", True, False)

account_1 = Account(1, "Savings", 1000, client_1)
account_2 = Account(2, "Checking", 500, client_2)
account_3 = Account(3, "Savings", 2000, client_3)

client_1.display_info()
client_2.display_info()
client_3.display_info()
client_3.change_contact("john1@gmail.com")
client_3.display_info()

account_1.deposit(500)
account_2.deposit(200)

account_1.withdraw(300)
account_2.withdraw(100)

account_3.withdraw(5000)

account_1.display_balance()
account_2.display_balance()
account_3.display_balance()

transaction1 = Transaction(1, "Payment", 500, "Payment for groceries")
transaction2 = Transaction(2, "Transfer", 2000, "Transfer to savings")
transaction3 = Transaction(3, "Transfer", 1600, "Tranfer to friend's account")

transaction1.process()
transaction2.cancel()
transaction3.update_desc("Transfer to friend's savings account")

print(transaction3.desc)

print(transaction1.status)
print(transaction2.status)
print(transaction3.status)

branch1 = Branch(1, "abc Branch", "Adelaide", "0400000000")
branch2 = Branch(2, "xyz Branch", "City", "0400000001", "Open")
branch3 = Branch(3, "ijk Branch", "Mawson Lakes", "0400000002", "Open")

print(branch1.available)
print(branch2.available)
print(branch3.available)

branch1.open_branch()
branch3.close_branch()
branch2.change_phone("0400000003")

print(branch1.available)
print(branch2.available)
print(branch3.available)
