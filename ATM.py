account_balance = 1000  # Ug Shs.

# Main program
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        print(f"Your account balance is: Ug Shs. {account_balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: Ug Shs. "))
        if amount < 0:
            print("Invalid amount. Please enter a positive value.")
        else:
            account_balance += amount
            print(f"Deposited: Ug Shs. {amount}")
            print(f"New balance: Ug Shs. {account_balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: Ug Shs. "))
        if amount < 0:
            print("Invalid amount. Please enter a positive value.")
        elif amount > account_balance:
            print("Insufficient funds. Cannot withdraw.")
        else:
            account_balance -= amount
            print(f"Withdrew: Ug Shs. {amount}")
            print(f"New balance: Ug Shs. {account_balance}")
    elif choice == '4':
        print("Exiting the ATM. Thank you!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")