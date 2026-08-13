class Client:
    def __init__(self, identifier, name, contact, local, active):
        self.name = name
        self.id = identifier
        self.contact = contact
        # there might be different rules for local and international clients (citizenship)
        self.location = local
        self.active = active

    def change_contact(self, new_contact):
        self.contact = new_contact

    def display_info(self):
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

    def __str__(self):
        return (f"Client Identity Number: {self.id}. Client name is {self.name}, their preferred contact is {self.contact}. Is client a citizen? {self.location}. Is client currently active? {self.active}")

    def __repr__(self):
        return (f"Client (id={self.id}, name={self.name}, contact={self.contact}, location={self.location}, active={self.active}")
