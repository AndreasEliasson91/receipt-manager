from person import Person
from personal_register import PersonalRegister
from transaction import Transaction


class TransactionRegister:
    def __init__(self):
        self.__num_of_transactions = 0
        self.__transactions = []

    def get_number_of_transactions(self):
        return self.__num_of_transactions

    def print(self):
        """
        Print the transactions in certain format
        """
        print(f"Total transactions: {self.__num_of_transactions}\n")
        print("Date\tType\tName\tAmount\tPersons\tNames")
        for i in range(self.__num_of_transactions):
            self.__transactions[i].print()

    def read(self, file):
        """
        Reads the file containing the transactions.
        Then creates objects of the Transaction class from each transaction, and appends them to self.__transactions.
        """
        for line in file:
            line = line.split()
            t = Transaction(line[0], line[1], line[2], float(line[3]), int(line[4]))
            for i in range(t.get_num_of_persons()):
                t.persons.append(line[i + 5])
            self.__transactions.append(t)
            self.__num_of_transactions += 1

    def add_transaction(self, t: Transaction):
        """
        Append a Transaction object to the register and increment the total number of transactions in it
        :param t: The Transaction object to append
        """
        self.__transactions.append(t)
        self.__num_of_transactions += 1

    def total_amount(self) -> float:
        """
        Calculates the total amount for all transactions
        :return: A temporary float containing the total amount
        """
        temp = 0.0
        for i in range(self.__num_of_transactions):
            temp += self.__transactions[i].get_amount()
        return temp

    def debt(self, name: str) -> float:
        """
        Calculates the total debt for a person, from all transaction they involved in but not paid for
        :param name: The name of the person
        :return: A temporary float containing the total debt
        """
        temp = 0.0
        for i in range(self.__num_of_transactions):
            if self.__transactions[i].find_person(name):
                temp += self.__transactions[i].get_amount() / (self.__transactions[i].get_num_of_persons() + 1)
        return temp

    def amount_paid(self, name: str) -> float:
        """
        Calculates the amount a person has paid and removes their own cost from the transaction
        :param name: The name of the person that made the transaction
        :return: A temporary float containing the total amount
        """
        temp = 0.0
        for i in range(self.__num_of_transactions):
            if self.__transactions[i].get_name() == name:
                temp += self.__transactions[i].get_amount() * (1.0 - 1.0 / (self.__transactions[i].get_num_of_persons() + 1))
        return temp

    def create_personal_register(self) -> PersonalRegister:
        """
        Creates, from Person objects, and returns an object of the class PersonalRegister
        :return: A PersonalRegister object
        """
        temp_list = PersonalRegister()
        for i in range(self.__num_of_transactions):
            if not temp_list.find_person(self.__transactions[i].get_name()):
                n = self.__transactions[i].get_name()
                person = Person(n, self.amount_paid(n), self.debt(n))
                temp_list.add_person(person)
        return temp_list

    def write(self, in_file: str):
        with open("./TransactionFiles/" + in_file, "w", encoding="utf-8") as out_file:
            out_file.writelines([self.__transactions[i] for i in range(self.__num_of_transactions)])
