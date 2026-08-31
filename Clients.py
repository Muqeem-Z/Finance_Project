from Accounts import Account
from Branches import Branch


class Client:
    """Represents a bank client and manages their contact details,
    account holdings, and preferred branch."""

    def __init__(self, identifier, name, contact, local, active):
        if isinstance(name, str) and name.strip():
            self.__name = name
        else:
            print("Invalid name. Using 'Unknown'.")
            self.__name = "Unknown"

        if isinstance(identifier, int) and not isinstance(identifier, bool) and identifier > 0:
            self.__id = identifier
        else:
            print("Invalid client ID. Using default ID of 0.")
            self.__id = 0

        if isinstance(contact, str) and contact.strip():
            self.__contact = contact
        else:
            print("Invalid contact. Using 'Unknown'.")
            self.__contact = "Unknown"

        # there might be different rules for local and international clients (citizenship)
        if isinstance(local, bool):
            self.__location = local
        else:
            print("Invalid location value. Using False.")
            self.__location = False

        if isinstance(active, bool):
            self.__active = active
        else:
            print("Invalid active value. Using False.")
            self.__active = False

        # A client begins with no accounts and no preferred branch.
        self.__accounts = []
        self.__preferred_branch = None

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_contact(self):
        return self.__contact

    def get_location(self):
        return self.__location

    def get_active(self):
        return self.__active

    def set_contact(self, new_contact):
        if isinstance(new_contact, str) and new_contact.strip():
            self.__contact = new_contact
        else:
            print("Invalid contact. Contact was not changed.")

    def set_active(self, new_active):
        if isinstance(new_active, bool):
            self.__active = new_active
        else:
            print("Invalid activity value. Activity was not changed.")

    def display_info(self):
        print("--------------------------------")
        print("          CLIENT INFO")
        print("--------------------------------")
        print(f"Client name: {self.__name}")
        print(f"Client identity number: {self.__id}")
        print(f"Client contact: {self.__contact}")
        print(f"Is client Australian? {self.__location}")
        print(f"Client Active: {self.__active}")
        print(f"Accounts held: {len(self.__accounts)}")
        if self.__preferred_branch is None:
            print("Preferred branch: None")
        else:
            print(
                f"Preferred branch: {self.__preferred_branch.get_branch_name()}")
        print("--------------------------------")

    def __str__(self):
        return (f"Client Identity Number: {self.__id}. Client name is {self.__name}, their preferred contact is {self.__contact}. Is client a citizen? {self.__location}. Is client currently active? {self.__active}")

    def __repr__(self):
        return (f"Client (id={self.__id}, name={self.__name}, contact={self.__contact}, location={self.__location}, active={self.__active}")

    def get_accounts(self):
        """Return a copy of the account list so the aggregation cannot be
        altered directly from outside the class."""
        return list(self.__accounts)

    def add_account(self, account):
        """Assign an existing Account object to this client."""
        if not isinstance(account, Account):
            print("Invalid object. Only Account objects can be added.")
        elif account in self.__accounts:
            print(
                f"Account {account.get_acc_id()} is already assigned to {self.__name}.")
        else:
            self.__accounts.append(account)
            print(f"Account {account.get_acc_id()} added to {self.__name}.")

    def remove_account(self, account):
        """Unassign an account without destroying the Account object."""
        if not isinstance(account, Account):
            print("Invalid object. Only Account objects can be removed.")
        elif account not in self.__accounts:
            print(f"That account is not assigned to {self.__name}.")
        else:
            self.__accounts.remove(account)
            print(
                f"Account {account.get_acc_id()} removed from {self.__name}.")

    def get_preferred_branch(self):
        return self.__preferred_branch

    def set_preferred_branch(self, branch):
        """Set the branch this client prefers to use."""
        if isinstance(branch, Branch):
            self.__preferred_branch = branch
            print(
                f"{self.__name}'s preferred branch is now {branch.get_branch_name()}.")
        else:
            print("Invalid object. Preferred branch was not changed.")
