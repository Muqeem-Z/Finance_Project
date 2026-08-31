class Transaction:
    """Represents a single financial transaction and manages its
    description and processing status."""

    def __init__(self, trans_id, trans_type, amount, desc):
        if isinstance(trans_id, int) and not isinstance(trans_id, bool) and trans_id > 0:
            self.__trans_id = trans_id
        else:
            print("Invalid transaction ID. Using default ID of 0.")
            self.__trans_id = 0

        if isinstance(trans_type, str) and trans_type.strip():
            self.__trans_type = trans_type
        else:
            print("Invalid transaction type. Using 'Unknown'.")
            self.__trans_type = "Unknown"

        if isinstance(amount, (int, float)) and not isinstance(amount, bool) and amount > 0:
            self.__amount = amount
        else:
            print("Invalid transaction amount. Using $0.00.")
            self.__amount = 0.0

        if isinstance(desc, str) and desc.strip():
            self.__desc = desc
        else:
            print("Invalid description. Using 'No description'.")
            self.__desc = "No description"

        self.__status = "Pending"

    def get_trans_id(self):
        return self.__trans_id

    def get_trans_type(self):
        return self.__trans_type

    def get_amount(self):
        return self.__amount

    def get_desc(self):
        return self.__desc

    def get_status(self):
        return self.__status

    def set_desc(self, new_desc):
        if isinstance(new_desc, str) and new_desc.strip():
            self.__desc = new_desc
            print("Transaction description updated.")
        else:
            print("Invalid description. Description was not changed.")

    def process(self):
        if self.__status == "Pending":
            self.__status = "Processed"
            print("Transaction has been processed.")
        else:
            print("Transaction cannot be processed because it is already settled.")

    def cancel(self):
        if self.__status == "Pending":
            self.__status = "Cancelled"
            print("Transaction has been cancelled.")
        else:
            print("Transaction cannot be cancelled because it is already settled.")

    def __str__(self):
        return (f"Transaction ID {self.__trans_id}. It is a {self.__trans_type} transaction containing amount ${self.__amount:.2f}, for {self.__desc}. Its current status is {self.__status}")

    def __repr__(self):
        return (f"Transaction (trans_id={self.__trans_id}, trans_type={self.__trans_type}, amount={self.__amount}, desc={self.__desc}, status={self.__status}")
