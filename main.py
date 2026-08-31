from Accounts import Account
from Clients import Client
from Transactions import Transaction
from Branches import Branch

# Create multiple objects of each type with different attribute values.
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

# Demonstrate the Client methods.
client_1.display_info()
client_2.display_info()
client_3.display_info()

print(client_3)
print(repr(client_3))

# Update the contact through the setter rather than by direct access.
client_3.set_contact("john1@gmail.com")

print(client_3)
print(repr(client_3))

client_3.display_info()

# Demonstrate the Account methods.
print(account_1)
print(repr(account_2))

account_1.deposit(500)
account_2.deposit(200)

account_1.withdraw(300)
account_2.withdraw(100)

print(account_1)
print(repr(account_2))

# A withdrawal larger than the balance is rejected.
account_3.withdraw(5000)

account_1.display_balance()
account_2.display_balance()
account_3.display_balance()

# Demonstrate the Transaction methods.
print(transaction3)
print(repr(transaction3))

transaction1.process()
transaction2.cancel()
transaction3.cancel()

transaction3.set_desc("Transfer to friend's savings account")

print(transaction3)
print(repr(transaction3))

# Demonstrate the Branch methods.
print(branch2)
print(repr(branch3))

branch1.open_branch()
branch3.close_branch()
branch2.set_phone("0400000003")

print(branch2)
print(repr(branch3))

# Demonstrate that invalid values are rejected without corrupting the object.
print("--- Validation ---")
client_1.set_contact(12345)
client_1.set_active("yes")
print(client_1)

account_1.set_acc_type("")
account_1.set_owner(99)
print(account_1)

transaction1.set_desc(None)
print(transaction1)

branch2.set_phone(400000004)
branch2.set_suburb("   ")
print(branch2)

# Demonstrate that the behaviour methods also validate their parameters
account_1.deposit(-200)
account_1.deposit("500")
account_1.deposit(True)
account_1.withdraw(0)
account_1.display_balance()

# Demonstrate the aggregation between Client and Account
print("--- Aggregation ---")
client_1.add_account(account_1)
client_1.add_account(account_2)
client_2.add_account(account_3)

# The same account cannot be assigned to a client twice.
client_1.add_account(account_1)

# Only Account objects are accepted by the relationship methods
client_1.add_account("Savings")
client_1.add_account(branch1)

# Removing an account from a client does not destroy the Account object.
client_1.remove_account(account_2)
print(account_2)

# Removing an account that was never assigned is handled safely
client_1.remove_account(account_3)

# Demonstrate the association between Client and Branch.
print("--- Association ---")
client_1.set_preferred_branch(branch1)
client_2.set_preferred_branch(branch2)

# An invalid object is rejected and the existing branch is retained.
client_1.set_preferred_branch("abc Branch")
print(client_1.get_preferred_branch())

# The preferred branch can be changed to a different Branch object.
client_1.set_preferred_branch(branch3)

# The branch objects remain independent of the clients that reference them.
print(branch1)
print(branch3)

# Show the final state of each client, including its relationships.
client_1.display_info()
client_2.display_info()
client_3.display_info()
