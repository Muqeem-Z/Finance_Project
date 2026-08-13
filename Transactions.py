class Transaction:
    def __init__(self, trans_id, trans_type, amount, desc):
        self.trans_id = trans_id
        self.trans_type = trans_type
        self.amount = amount
        self.desc = desc
        self.status = "Pending"

    def update_desc(self, new_desc):
        self.desc = new_desc
        print("Transaction description updated.")

    def process(self):
        if self.status == "Pending":
            self.status = "Processed"
            print("Transaction has been processed.")
        else:
            print("Transaction cannot be processed because it is already settled.")

    def cancel(self):
        if self.status == "Pending":
            self.status = "Cancelled"
            print("Transaction has been cancelled.")
        else:
            print("Transaction cannot be cancelled because it is already settled.")

    def __str__(self):
        return (f"Transaction ID {self.trans_id}. It is a {self.trans_type} transaction containing amount ${self.amount:.2f}, for {self.desc}. Its current status is {self.status}")

    def __repr__(self):
        return (f"Transaction (trans_id={self.trans_id}, trans_type={self.trans_type}, amount={self.amount}, desc={self.desc}, status={self.status}")
