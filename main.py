def main():
    # file_name = input("Enter the name of the file: ")
    file_name = "travel.txt"

    with open("./TransactionFiles/" + file_name, "r", encoding="utf-8") as file:
        t = file.readlines()

    print("Date\tType\tName\tAmount\tPersons\tNames")
    for i in t:
        print(i)


if __name__ == "__main__":
    main()
