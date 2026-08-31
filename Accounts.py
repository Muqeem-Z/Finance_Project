class Account:
    """Represents a single bank account and manages its balance
    through deposit and withdrawal behaviour."""

    def __init__(self, acc_id, acc_type, balance, owner):
        if isinstance(acc_id, int) and not isinstance(acc_id, bool) and acc_id > 0:
            self.__acc_id = acc_id
        else:
            print("Invalid account ID. Using default ID of 0.")
            self.__acc_id = 0

        if isinstance(acc_type, str) and acc_type.strip() != "":
            self.__acc_type = acc_type
        else:
            print("Invalid account type. Using default type 'Unknown'.")
            self.__acc_type = "Unknown"

        if isinstance(balance, (int, float)) and not isinstance(balance, bool) and balance >= 0:
            self.__balance = balance
        else:
            print("Invalid balance. Using default balance of $0.00.")
            self.__balance = 0.0

        if isinstance(owner, str) and owner.strip() != "":
            self.__owner = owner
        else:
            print("Invalid owner. Using default owner 'Unknown'.")
            self.__owner = "Unknown"

    def deposit(self, amount):
        """Add a valid amount to the balance."""
        if isinstance(amount, (int, float)) and not isinstance(amount, bool) and amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount. Deposit was rejected.")

    def withdraw(self, amount):
        """Remove a valid amount from the balance if funds allow."""
        if not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount <= 0:
            print("Invalid withdrawal amount. Withdrawal was rejected.")
        elif amount > self.__balance:
            print(
                f"Account {self.__acc_id} has insufficient funds for this withdrawal.")
        else:
            self.__balance -= amount

    def display_balance(self):
        print(f"{self.__acc_id}'s account balance: ${self.__balance:.2f}")

    def get_acc_id(self):
        return self.__acc_id

    def get_acc_type(self):
        return self.__acc_type

    def get_balance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner

    def set_acc_type(self, new_type):
        if isinstance(new_type, str) and new_type.strip() != "":
            self.__acc_type = new_type
        else:
            print("Invalid account type. Account type was not changed.")

    def set_owner(self, owner):
        if isinstance(owner, str) and owner.strip() != "":
            self.__owner = owner
        else:
            print("Invalid owner. Owner was not changed.")

    def __str__(self):
        return (
            f"Account ID {self.__acc_id} belongs to {self.__owner}. "
            f"It is a {self.__acc_type} account with a balance of "
            f"${self.__balance:.2f}"
        )

    def __repr__(self):
        return (
            f"Account(acc_id={self.__acc_id}, "
            f"acc_type={self.__acc_type}, "
            f"balance={self.__balance}, "
            f"owner={self.__owner})"
        )
