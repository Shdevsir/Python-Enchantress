from random import randint


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=SingletonMeta):
    def __init__(self, name, houses, discount, lst=None):
        self.name = name
        self.houses = houses
        self.discount = discount
        self.lst = lst or []

    def give_discount(self):
        print(f'Realtor: Your discount is {self.discount}%')
        for x in self.lst:
            x.cost = x.cost - x.cost * (self.discount * 0.01)

    def information_about_houses(self):
        cnt = 0
        for x in self.lst:
            cnt += 1
            print(f'House {cnt}: area {x.area} cost: {x.cost}')

    @staticmethod
    def steal_money(human):
        rand = randint(1, 10)
        if rand == 1:
            human.money = human.money - human.money * 0.1
            print(f'Now {human.name} have {human.money}$')
        else:
            print('Sorry realtor, you don`t steal money')


class Person:
    def __init__(self, name, age, money, home):
        self.name = name
        self.age = age
        self.money = money
        self.home = home


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost


class Human(Person, House):
    def provide_information(self):
        print(
            f" Name: {self.name}\n Age: {self.age}\n Availability of money: {self.money}$\n \
Having your own home: {self.home}")

    def make_money(self, cash):
        print(f'Okey, i see you need {cash}$')
        if cash >= 0:
            day = round((cash / 10) / 24, 1)
            print('You go to work as a cashier for 10$ per hour')
            self.money = self.money + cash
            print(f'You work {day} days, now your money is {self.money}$')

    def buy_house(self, obj):
        if 30 >= obj.area >= 10:
            house = 'small_house'
        elif obj.area <= 40:
            house = 'medium_house'
        elif obj.area > 40:
            house = 'big_house'
        else:
            house = 'cardboard box'
        if obj.cost <= self.money:
            print(f'Congratulations, now you home is {house}')
            self.home = house
            self.money = self.money - obj.cost
        else:
            print('Sorry you don`t have money')


class Home(House):
    def apply_discount(self, discount):
        print(f' Home: Your discount is {discount}%')
        self.cost = self.cost - self.cost * (discount * 0.01)
        print(f' Home: Now cost is {self.cost}')


if __name__ == '__main__':
    person = Human('Jhon', 35, 2000, 'Home_old')
    person.provide_information()
    small_house1 = Home(40, 2000)
    small_house2 = Home(30, 1500)
    small_house3 = Home(20, 1000)
    small_house1.apply_discount(5)
    list_of_house = [small_house1, small_house2, small_house3]
    realtor = Realtor('Mr.Cary', 3, 5, list_of_house)
    person.make_money(100)
    person.buy_house(small_house3)
    person.provide_information()
    realtor.information_about_houses()
    realtor.give_discount()
    realtor.information_about_houses()
    realtor.steal_money(person)
