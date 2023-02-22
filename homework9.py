# Exersice 1
# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від
# "Транспортний засіб". Наповніть класи атрибутами на свій розсуд. Створіть обʼєкти класів "Автомобіль",
# "Літак", "Корабель".

class Vehicle:
    """Simple vehicle modeling"""
    def __init__(self, vehicle_type):
        """Initialize attributes name and type"""
        self.vehicle_type = vehicle_type

    """Return vehicle type"""
    def get_vehicle_type(self):
        return f'This vehicle refers to {self.vehicle_type}.'

class Car(Vehicle):
    """Initialize attributes which describes the car"""
    make = 'audi'
    model = 'q8'
    year = 2020

    """Return formatted name"""
    def get_descriptive_name(self):
        long_name = (f'Car information: {self.make}, {self.model}, {self.year}')
        return long_name.title()

class AirPlain(Vehicle):
    """Initialize attributes which describes the airplain"""
    make = 'Мрія'
    model = 'Ан-225'
    year = 1988

    """Return formatted name"""
    def get_descriptive_name(self):
        long_name = (f'Airplain information: {self.make}, {self.model}, {self.year}')
        return long_name.title()

class Ship(Vehicle):
    """Initialize attributes which describes the airplain"""
    make = 'Титанік'
    model = 'RMS Titanic'
    year = 1908

    """Return formatted name"""

    def get_descriptive_name(self):
        long_name = (f'Airplain information: {self.make}, {self.model}, {self.year}')
        return long_name.title()

my_car = Car('car')
print(my_car.get_vehicle_type())
print(my_car.get_descriptive_name())

my_airplain = AirPlain('airplain')
print(my_airplain.get_vehicle_type())
print(my_airplain.get_descriptive_name())

my_ship = Ship('ship')
print(my_ship.get_vehicle_type())
print(my_ship.get_descriptive_name())
