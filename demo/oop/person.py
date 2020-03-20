class InvalidAgeError(Exception):
    def __init__(self,age):
        self.message = f"Invalid Age --> {age}"

    def __str__(self):
        return self.message

class Person:
    def __init__(self, name, age):
        self.name = name
        if age > 120:
            raise InvalidAgeError(age)
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        print("__eq__")
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    def __int__(self):
        return self.age


try:
    p1 = Person("Abc", 130)
except Exception as ex:
    print(ex)

p2 = Person("Abc", 20)
p3 = Person("Xyz", 20)
# print(str(p1))
# print(p1 == p2, p1 != p3)
# print(p1 > p2)    # p1.__gt__(p2)
# print(int(p1) + int(p2))
