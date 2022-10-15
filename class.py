import os.path
import pysnooper


class Dog:
    """Модель собаки"""

    def __init__(self, name: str, age=None):
        """

        :param name: Name dog
        :param age: Age dog
        """
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится"""
        return f'{self.name} садится'

    def __str__(self) -> str:
        return f"Имя: {self.name}, Возраст: {self.age}"


# my_pet = Dog('Vasya')
# print(my_pet.sit())


class Car:
    def __init__(self, make: str, model: str, year: int, odometer=0):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer

    def __str__(self) -> str:
        return f"Marka: {self.make}\n Model: {self.model}\n God: {self.year}"

    def get_odometer(self):
        return f'Probeg: {self.odometer} km'

    def add_odometr(self, km):
        self.odometer += km


class ElectricCar(Car):
    def __init__(self, make, model, year, odometer, battery_size: int):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def get_power_reservre(self):
        if self.battery_size < 75:
            return "Запас хода: < 200 km"
        else:
            return "Запас хода: > 200 km"


# car_1 = Car("BMW", "X5", 2019, 25000)
# car_2 = ElectricCar("Tesla", "Model 3", 2021, 15000, 85)

# print(car_1)
# car_1.add_odometr(100)
# print(car_1.get_odometer())
#
# print(car_2)
# print(car_2.get_odometer())
"""Работа с файлами

r - только для чтения
r+ - для записи и чтения
w - только для записи (создаст новый файл стаким именем не найден)
w+ - для чтения и записи (создаст новый файл стаким именем не найден)
rb - чтения бинарного файла
wb - только для записи в .bin файл
a - откроет файл дл\я добавления новой информации (создаст новый файл стаким именем не найден)
"""


@pysnooper.snoop()
def writer(name: str, param: str):
    if not os.path.exists('files'):
        os.mkdir('files')

    with open(r'files\some_file.txt', f'{param}', encoding='utf-8') as file:
        file.write(f'Привет меня зовут {name.title()}\n')

def reader():
    with open(r'files\some_file.txt', 'r', encoding='utf-8')as file:
        # text = file.read()
        text = file.readline()


reader()
