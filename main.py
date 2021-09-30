from personal_register import PersonalRegister
from transaction import Transaction
from transaction_register import TransactionRegister


def main():
    transaction_register = TransactionRegister()
    transaction_register.read()

    while True:
        print("============\n\tMENU\n============\n\n0. Quit and save transactions to a file\n1 Print information about"
              " the transactions in the file\n2. Read a transaction from input\n3. Calculate the total cost\n"
              "4. Calculate a certain persons debt\n5. Calculate a certain persons total amount paid\n"
              "6. List all persons and fix\n")
        option = int(input("Choose an option from the menu: "))
        print()

        if option == 0:
            break
        elif option == 1:
            transaction_register.print()
        elif option == 2:
            transaction = Transaction()
            transaction.read()
            transaction_register.add_transaction(transaction)
        elif option == 3:
            print(f"The total amount of all transactions is: {transaction_register.total_amount()}")
        elif option == 4:
            name = input("Enter the name to see the total debt: ")
            debt = transaction_register.debt(name)
            if debt == 0.0:
                print(f"Can't find {name} in the register")
            else:
                print(f"{name}'s total debt is {debt}")
        elif option == 5:
            name = input("Enter the name to see how much they paid: ")
            paid = transaction_register.amount_paid(name)
            if paid == 0.0:
                print(f"Can't find {name} in the register")
            else:
                print(f"{name} has paid a total of {paid}")
        elif option == 6:
            personal_register = transaction_register.create_personal_register()
            personal_register.print()
        else:
            print("Invalid input. Try again!")


if __name__ == "__main__":
    main()
