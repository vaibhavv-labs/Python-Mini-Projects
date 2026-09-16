print("="*35)
print("---------Mini ATM---------")
print("="*35)

balance = 5000

while True:
    print("\n 1. Check Balance : ")
    print("\n 2. Windraw Amount :")
    print("\n 3. Deposite :")
    print("\n 4. Exit :")

    choice = input("Choose an Operation :")

    if choice == "1":
        print("Balance :", balance)
    elif choice == "2":
        amount = int(input("\n Enter Amount :"))
        if amount <= balance:
            balance -= amount
            print("\n windraw amount successful")
            print("\n Remaining Balance :", balance)
        else:
            print("Insufficiant Balance !!")

    elif choice == "3":
        amount = int(input("Enter Deposite Amount :"))
        balance += amount
        print("\n deposite Successfull")

    elif choice == "4":
        print("Thank you")
        break

    else:
        print("Invalid Option")

print("Have a Good Day")
