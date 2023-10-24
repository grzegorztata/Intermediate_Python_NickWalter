import random

class Dog:
    info = "A little fury creature"

    def __init__(self, name):
        print("I am alive")
        self.lucky_number = random.randint(1,10)
        self.name = name

dog1 = Dog("Frido")
dog2 = Dog("Sara")

print(dog1.name)
print(dog2.name)