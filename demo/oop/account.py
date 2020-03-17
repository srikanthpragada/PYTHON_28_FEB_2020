class Account:
    # class attribute
    minbal = 5000

    @staticmethod
    def set_minbal(minbal):
        Account.minbal = minbal

    @staticmethod
    def get_minbal():
        return Account.minbal

    # Constructor
    def __init__(self, acno, ahname, balance=0):
        # Object attributes
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - Account.minbal >= amount:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def print_details(self):
        print("Acno    : ", self.acno)
        print("Ahname  : ", self.ahname)
        print("Balance : ", self.balance)


# Account.set_minbal(10000)
a = Account(1, "Scott", 10000)  # Create an object
a.withdraw(5000)
a.print_details()