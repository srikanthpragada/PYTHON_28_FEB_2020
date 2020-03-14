class Account:
    # Constructor
    def __init__(self, acno, ahname, balance=0):
        # Object attributes
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def print_details(self):
        print("Acno    : ", self.acno)
        print("Ahname  : ", self.ahname)
        print("Balance : ", self.balance)


a = Account(1, "Scott", 10000)  # Create an object
print(a.__dict__)
a.deposit(20000)
a.print_details()

a2 = Account(2, "Tom")
