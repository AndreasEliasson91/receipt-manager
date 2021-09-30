def main():
    with open("./TransactionFiles/travel.txt", "r", encoding="utf-8") as file:
        t = file.readlines()
        print(t)


if __name__ == "__main__":
    main()
