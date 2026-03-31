balance = 10000

while True:
    print("\n ATM MENU ")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Updated Balance:", balance)

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient Balance ❌")
        else:
            balance -= amount
            print("Remaining Balance:", balance)

    elif choice == 4:
        print("Thank you 🙌")
        break

    else:
        print("Invalid choice ⚠️")