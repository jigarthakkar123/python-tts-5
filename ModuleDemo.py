import Udf

while True:

    print("*"*50)
    print("1. OddEven")
    print("2. MaxOfTwo")
    print("3. MaxOfThree")
    print("4. Prime")
    print("5. Fibonacci")
    print("6. Exit")
    print("*"*50)
    choice=int(input("Enter Your Choice : "))
    print("*"*50)

    if choice==1:
        a=int(input("Enter Value : "))
        Udf.oddeven(a)
        print("*"*50)
    elif choice==2:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        Udf.maxoftwo(a,b)
        print("*"*50)
    elif choice==3:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        c=int(input("Enter Value : "))
        Udf.maxofthree(a,b,c)
        print("*"*50)
    elif choice==4:
        a=int(input("Enter Value : "))
        Udf.prime(a)
        print("*"*50)
    elif choice==5:
        a=int(input("Enter Value : "))
        Udf.fibonacci(a)
        print("*"*50)
    elif choice==6:
        print("Thanks For Using Our Services")
        print("*"*50)
        break
    else:
        print("Invalid Choice")
        print("*"*50)
