class Bank:
    acc_no=int
    balance=int
    ac_type=str
    cust_no=str
    def __init__(self,acc_no,balance,ac_type,cust_no):
        self.acc_no=acc_no
        self.balance=balance
        self.ac_type=ac_type
        self.cust_no=cust_no
    def deposit(self,amount):
        self.balance+=amount
        print(f"your acc {self.acc_no}has been credited with amount{amount}avl bal{self.balance}")
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"your acc {self.acc_no}has been debited with amount{amount}avl bal{self.balance}")
        else:
            print("insufficent")
    def get_balance(self):
        print("your aval bal",self.balance)

bank1=Bank(100,5000,"permanant","ananthu")
bank1.withdraw(1500)


