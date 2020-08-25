import datetime
class Bank:
    def __init__(self,accno,pname):
        self.accno=accno
        self.pname=pname
        self.balance=3000
        self.bname="sbk"
    def deposit(self,amt):
        self.balance+=amt
        print("your account",self.accno,"has been credited with",amt,datetime.date.today())


    def withdraw(self,amt):
        if(amt>self.balance):
            print("insufficient balance")
        else:
            self.balance-=amt
            print("your account",self.accno," has been debited with :",amt,datetime.date.today())


    def printBalance(self):
        print("current balance :",self.balance)


obj=Bank(1001,"jane")

obj.deposit(5000)
obj.printBalance()
obj.withdraw(5000)
obj.printBalance()
obj.withdraw(5000)