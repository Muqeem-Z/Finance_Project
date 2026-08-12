from Accounts import Account
from Clients import Client

client_1 = Client(1, "Ali", "ali@gmail.com", True, True)
client_2 = Client(2, "Sarah", "0412345679", False, True)
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