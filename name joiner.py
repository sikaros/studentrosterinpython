# simple program that asks for your first and then your last name and outputs it together.
class NameStruct:
    def __init__(self):
        self._first_name = ""
        self._last_name = ""

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    def get_full_name(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    def __str__(self):
        return self.get_full_name()


def main():
    ns = NameStruct()

    first_name_input = input("Enter your first name: ")
    last_name_input = input("Enter your last name: ")

    ns.first_name = first_name_input
    ns.last_name = last_name_input

    # Print the first name and last name on separate lines
    print("First Name:")
    print(ns.first_name)
    print("Last Name:")
    print(ns.last_name)

    print(ns)


if __name__ == "__main__":
    main()
