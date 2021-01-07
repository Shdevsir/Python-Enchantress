import random

ANIMAlS = {
    'Types': {0: 'Fish', 1: 'Mammal', 2: 'Bird'},
    'Location': {0: 'Water', 1: 'Land', 2: 'Air'}
}


class Animal:
    def __init__(self, type_of_animal, age):
        self.type_of_animal = type_of_animal
        self.age = age

    def get_type(self):
        print('The type of animal is ' + ANIMAlS['Types'][self.type_of_animal])

    def get_location(self):
        print('The location is ' + ANIMAlS['Location'][self.type_of_animal])

    def get_maturity(self):
        if self.age <= 1:
            print('This animal is baby')
        else:
            print('This animal is grown')


class Wolf(Animal):
    def jump_to_hunt(self):
        if self.age >= 1:
            print('Start hunting')
        else:
            print('Sorry animal is not grown')


class Dog(Wolf, Animal):
    @staticmethod
    def woof():
        print('Woof')


class Eagle(Animal):
    @staticmethod
    def fly_in_air():
        random_number = random.randrange(1000)
        print(f'Took of into the sky on {random_number} meters')


class Perch(Animal):
    @staticmethod
    def eat_seaweed():
        print('Eating...')


class GoldFish(Perch, Animal):
    @staticmethod
    def make_dreams(dream):
        print(f'{dream} will come true')


if __name__ == '__main__':
    goldfish = GoldFish(0, 2)
    goldfish.get_type()
    goldfish.get_maturity()
    goldfish.get_location()
    goldfish.make_dreams('1000$')
    goldfish.eat_seaweed()
