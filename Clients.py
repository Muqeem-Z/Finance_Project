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

    def __str__ (self):
        return (f"Client Identity Number: {self.id}, Name: {self.name}, Preffered Contact: {self.contact}")

