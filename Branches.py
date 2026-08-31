class Branch:
    """Represents a physical bank branch and manages its contact
    details and opening state."""

    def __init__(self, branch_num, branch_name, suburb, phone, available="Closed"):
        if isinstance(branch_num, int) and not isinstance(branch_num, bool) and branch_num > 0:
            self.__branch_num = branch_num
        else:
            print("Invalid branch number. Using default number of 0.")
            self.__branch_num = 0

        if isinstance(branch_name, str) and branch_name.strip():
            self.__branch_name = branch_name
        else:
            print("Invalid branch name. Using 'Unknown'.")
            self.__branch_name = "Unknown"

        if isinstance(suburb, str) and suburb.strip():
            self.__suburb = suburb
        else:
            print("Invalid suburb. Using 'Unknown'.")
            self.__suburb = "Unknown"

        if isinstance(phone, str) and phone.strip():
            self.__phone = phone
        else:
            print("Invalid phone number. Using 'Unknown'.")
            self.__phone = "Unknown"

        if isinstance(available, str) and available in ["Open", "Closed"]:
            self.__available = available
        else:
            print("Invalid availability. Using 'Closed'.")
            self.__available = "Closed"

    def get_branch_num(self):
        return self.__branch_num

    def get_branch_name(self):
        return self.__branch_name

    def get_suburb(self):
        return self.__suburb

    def get_phone(self):
        return self.__phone

    def get_available(self):
        return self.__available

    def open_branch(self):
        if self.__available == "Closed":
            self.__available = "Open"
            print("Branch has been opened.")
        else:
            print("Branch is already open.")

    def close_branch(self):
        if self.__available == "Open":
            self.__available = "Closed"
            print("Branch has been closed.")
        else:
            print("Branch is already closed.")

    def set_phone(self, number):
        if isinstance(number, str) and number.strip():
            self.__phone = number
            print(f"Phone number has been changed to {self.__phone}.")
        else:
            print("Invalid phone number. Phone number was not changed.")

    def set_branch_name(self, branch_name):
        if isinstance(branch_name, str) and branch_name.strip():
            self.__branch_name = branch_name
        else:
            print("Invalid branch name. Branch name was not changed.")

    def set_suburb(self, suburb):
        if isinstance(suburb, str) and suburb.strip():
            self.__suburb = suburb
        else:
            print("Invalid suburb. Suburb was not changed.")

    def __str__(self):
        return (f"Branch Number: {self.__branch_num}. Branch name is {self.__branch_name}, located in {self.__suburb}. Their contact details are {self.__phone}. Branch is currently {self.__available}")

    def __repr__(self):
        return (f"Branch (branch_num={self.__branch_num}, branch_name={self.__branch_name}, suburb={self.__suburb}, phone={self.__phone}, available={self.__available}")
