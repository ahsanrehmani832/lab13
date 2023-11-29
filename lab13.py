class Person:
    def __init__(self, name, age, address):
        self._name = name
        self._age = age
        self._address = address

    # Getter and setter for name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and setter for age
    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    # Getter and setter for address
    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

# Example usage:
# Create a person
person = Person(name="Ahsan Rehmani", age=22, address="Johar town lahore")

# Access and modify attributes using getter and setter methods
print("Name:", person.get_name())
print("Age:", person.get_age())
print("Address:", person.get_address())

person.set_name("Ahsan Rehmani")
person.set_age(22)
person.set_address("Johar town lahore")

print("\nUpdated Information:")
print("Name:", person.get_name())
print("Age:", person.get_age())
print("Address:", person.get_address())
