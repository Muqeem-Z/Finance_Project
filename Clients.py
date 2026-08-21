class Client:
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

    def set_active (self, new_active):
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
        print("--------------------------------")
        print("")

    def __str__(self):
        return (f"Client Identity Number: {self.__id}. Client name is {self.__name}, their preferred contact is {self.__contact}. Is client a citizen? {self.__location}. Is client currently active? {self.__active}")

    def __repr__(self):
        return (f"Client (id={self.__id}, name={self.__name}, contact={self.__contact}, location={self.__location}, active={self.__active}")
