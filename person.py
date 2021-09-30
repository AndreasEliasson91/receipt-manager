class Person:
    def __init__(self, name: str, amount_paid: float, debt: float):
        self.__name = name
        self.__amount_paid = amount_paid
        self.__debt = debt

    def get_name(self):
        return self.__name

    def get_amount_pad(self):
        return self.__amount_paid

    def get_debt(self):
        return self.__debt

