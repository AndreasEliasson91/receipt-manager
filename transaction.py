class Transaction:
    def __init__(self, date="", type="", name="", amount=0.0, num_of_persons=0):
        self.__date = date
        self.__type = type
        self.__name = name
        self.__amount = amount
        self.__num_of_persons = num_of_persons
        self.persons = []

    def get_name(self):
        return self.__name

    def get_amount(self):
        return self.__amount

    def get_num_of_persons(self):
        return self.__num_of_persons

    def print(self):
        print(f"{self.__date}\t{self.__type}\t{self.__name}\t{self.__amount}\t{self.__num_of_persons}", end="\t")
        for i in range(self.__num_of_persons):
            print(self.persons[i], end=" ")
        print()

    def read(self):
        self.__date = input("Enter the following information about the transaction\nDate (YY/MM/DD): ")
        self.__type = input("Type (food, rent etc.): ")
        self.__name = input("Name of the person who executed the transaction: ")
        self.__amount = float(input("Total cost: "))
        self.__num_of_persons = int(input("Enter how many persons that will split the cost: "))
        print("Enter their names: ")
        for _ in range(self.__num_of_persons):
            self.persons.append(input())

    def find_person(self, name: str) -> bool:
        """
        Function to search the list of names involved in the transaction after a pre-determent name
        :param name: Name to search for
        :return: True if the name is found else False
        """
        for i in range(self.__num_of_persons):
            if self.persons[i] == name:
                return True
        return False
