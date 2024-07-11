class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def display(self):
        print(f"Name = {self.name}, Age = {self.age}")

user_name = input("Enter the person's name: ")
user_age = int(input("Enter the person's age: "))
person1 = Person(name=user_name, age=user_age)

print("Before Birthday:")
person1.display()

person1.birthday()
print("After Birthday:")
person1.display()
