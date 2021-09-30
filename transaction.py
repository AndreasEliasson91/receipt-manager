class Transaction:
    def __init__(self, date: int, type: str, name: str, amount: int, num_of_persons: int, persons: list):
        self.__date = date
        self.__type = type
        self.__name = name
        self.__amount = amount
        self.__num_of_persons = num_of_persons
        self.__persons = persons

    def get_name(self):
        return self.__name

    def get_amount(self):
        return self.__amount

    def get_num_of_persons(self):
        return self.__num_of_persons
