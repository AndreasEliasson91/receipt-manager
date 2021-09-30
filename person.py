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

    def print(self):
        print(f"{self.__name} has paid {self.__amount_paid} and has debt of {self.__debt}.")
        if (self.__amount_paid - self.__debt) >= 0.0:
            print(f"{self.__name} shall have {(self.__amount_paid - self.__debt)} from the pot.")
        else:
            print(f"{self.__name} shall pay {(self.__debt - self.__amount_paid)} to the pot.")
