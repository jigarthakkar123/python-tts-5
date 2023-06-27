class Bank:

    def openAccount(self,cname,acno,balance):
        self.c=cname
        self.ac=acno
        self.b=balance
        print("Hello ",self.c,", Your Account Number ",self.ac," Is opened With ",self.b," Rs.")
    def deposit(self,amount):
        self.b=self.b+amount
    def withdraw(self,amount):
        if amount<=self.b:
            self.b=self.b-amount
        else:
            self.needs=amount-self.b
            print("Sorry You Need Another ",self.needs," Rs. To Withdraw")
    def checkBalance(self):
        print("Current Balance : ",self.b)

print("*"*60)
b1=Bank()
cname=input("Enter Customer Name : ")
print("*"*60)
acno=int(input("Enter Account Number : "))
print("*"*60)
balance=int(input("Enter Initial Balance : "))
print("*"*60)
b1.openAccount(cname,acno,balance)
print("*"*60)

while True:

    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*60)
    choice=int(input("Enter Your Choice : "))
    print("*"*60)
    if choice==1:
        amount=int(input("Enter Deposit Amount : "))
        b1.deposit(amount)
        print("*"*60)
    elif choice==2:
        amount=int(input("Enter Withdrawal Amount : "))
        b1.withdraw(amount)
        print("*"*60)
    elif choice==3:
        b1.checkBalance()
        print("*"*60)
    else:
        print("Thank You For Using Our Services.Good Bye")
        print("*"*60)
        break
