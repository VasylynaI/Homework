# Exersice 1
# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від
# "Транспортний засіб". Наповніть класи атрибутами на свій розсуд. Створіть обʼєкти класів "Автомобіль",
# "Літак", "Корабель".

class Vehicle:
    """Simple vehicle modeling"""
    def __init__(self, vehicle_type, make, modal, year):
        """Initialize attributes type, make, modal, year"""
        self.vehicle_type = vehicle_type
        self.make = make
        self.modal = modal
        self.year = year


    def get_vehicle_descriptive(self):
        """Return vehicle type and detail information"""
        return f'This vehicle refers to {self.vehicle_type}. Detail information:' \
               f' {self.make}, {self.modal}, {self.year}.'

class Car(Vehicle):
    """Initialize attributes which describes the car fuel type"""
    fuel_type = 'diesel'

    def get_fuel_descriptive(self):
        """Return fuel descriptive"""
        return f'fuel type - {self.fuel_type}'

class AirPlain(Vehicle):
    """Initialize attributes which describes the wingspan"""
    wingspan = '88 meters'

    def get_wingspan_descriptive(self):
        """Return wingspan descriptive"""
        return f'Wingspan - {self.wingspan} meters'

class Ship(Vehicle):
    """Initialize attributes which describes the ship length"""
    length = 120

    def get_length_descriptive(self):
        """Return length descriptive"""
        return f"Length - {self.length} meters"


my_car = Car('car', 'audi', 'q8', 2020)
print(my_car.get_vehicle_descriptive())
print(my_car.get_fuel_descriptive())

my_airplain = AirPlain('airplain', 'Мрія', 'Ан-225', 1988)
print(my_airplain.get_vehicle_descriptive())
print(my_airplain.get_wingspan_descriptive())

my_ship = Ship('ship', 'Titanic', 'RMS ', 1908)
print(my_ship.get_vehicle_descriptive())
print(my_ship.get_length_descriptive())
