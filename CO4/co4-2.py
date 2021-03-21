class Bank:
    def __init__(self, bal):
        self.bal = bal

    def deposit(self):
        amt = float(input("Enter the amount to be deposited:"))
        self.bal = self.bal+amt
        print("balance:", self.bal)
        return self.bal

    def withdraw(self):
        amt = float(input("Enter the amount to be withdrawn"))
        if amt > b1.bal:
            print("Insufficient Balance!!")
        else:
            b1.bal = b1.bal - amt
            print("balance:", b1.bal)
        return b1.bal


b1 = Bank(0)
b2 = Bank(0)
b1.deposit()
b2.withdraw()
