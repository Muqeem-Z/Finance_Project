class Branch:
    def __init__(self, branch_num, branch_name, suburb, phone, available = "Closed"):
        self.branch_num = branch_num
        self.branch_name = branch_name
        self.suburb = suburb
        self.phone = phone
        self.available = available

    def open_branch(self):
        if self.available == "Closed":
            self.available = "Open"
            print("Branch has been opened.")
        else:
            print("Branch is already open.")

    def close_branch(self):
        if self.available == "Open":
            self.available = "Closed"
            print("Branch has been closed.")
        else:
            print("Branch is already closed.")

    def change_phone(self, number):
        self.phone = number
        print(f"Phone number has been changed to {self.phone}.")
