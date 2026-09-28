# python oop - inheritance
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("i don't know what to say")

    def show(self):
        print(f"i am {self.name}, i'm {self.age} years old")


class Fish(Pet):
    pass

class Dog(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show(self):
        print(f"i'm {self.name}, i'm {self.age} years old and i am {self.color}")

    def speak(self):
        print("bark")

class Cat(Pet):
    def speak(self):
        print("meow ")


d = Dog("bill", 12, "white")
d.show()


p = Pet("tim", 12)
p.show()

d = Dog("lil", 9, "brown")
d.show()

c = Cat("lola", 7)
c.show()

f = Fish("bubble", 21)
f.speak()


# class attributes
class Person:
    number_of_people = 10

    def __init__(self, name) -> None:
        self.name = name
        Person.number_of_people += 1


p1 = Person("ayush")
print(p1.number_of_people)
p2 = Person("gojo")
print(Person.number_of_people)
