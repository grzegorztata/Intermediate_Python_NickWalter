import random

class Dog:
    info = "A furry little creature"

    def __init__(self):
        print("I'm alive!")
        print(random.randint(1,10))
        self.lucky_number = random.randint(50,100)

print('---- Standardowe użycie ----')
print(Dog.info)
Dog()

print('---- Instancje ----')
dog1 = Dog()
dog2 = Dog()
print('--- Only numbers ----')
print(dog1.lucky_number)
print(dog2.lucky_number)

print('---- Przypisanie imienia do klasy ----')
dog1.name = "Frido"
print(dog1.name)

###########
