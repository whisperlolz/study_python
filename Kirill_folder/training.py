# from pkgutil import get_data
#
#
# class Cat:
#     name = None
#     age = None
#     isHappy = None
#
#     def __init__(self, name, age, isHappy):
#         self.set_data(name, age, isHappy)
#         self.get_data()
#
#     def set_data(self, name=None, age=None, isHappy=None):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
#
#     def get_data(self):
#         print(f"Name: {self.name}\nAge: {self.age}\nIsHappy: {self.isHappy}")
#
#
# cat_one = Cat("Szarik", 3, True)
# cat_one.set_data("John", 2)
#
# cat_two = Cat("Bobik", 2, False)


class Building:
    __year = None
    __city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year: ", self.year, "; City: ", self.city)


class School(Building):
    pupils = 0

    def __init__(self, pupils, year, city):
        super(School, self).__init__(year, city)
        self.pupils = pupils

    def get_info(self):
        print("Year: ", self.year, "; City: ", self.city, "; Pupils: ", self.pupils)


class House(Building):
    pass


class Shop(Building):
    pass


school = School(100, 2000, "Gdansk")
school.get_info()
house = House(2000, "Gdansk")
shop = Shop(2000, "Gdansk")
shop.get_info()
