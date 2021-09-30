from person import Person


class PersonalRegister:
    def __init__(self):
        self.__num_of_persons = 0
        self.persons = []

    def print(self):
        for i in range(self.__num_of_persons):
            self.persons[i].print()

    def find_person(self, name: str) -> bool:
        """
        Function to search the list of Person objects after a pre-determent name
        :param name: Name to search for
        :return: True if the name is found else False
        """
        for i in range(self.__num_of_persons):
            if self.persons[i].get_name() == name:
                return True
        return False

    def add_person(self, p: Person):
        """
        Check if the Person object exists in the register,
        else append the Person object to the register and increment the total number of number of persons
        :param p: The Person object to append
        """
        if not self.find_person(p.get_name()):
            self.persons.append(p)
            self.__num_of_persons += 1
