"""ДЗ 16.1. Ромбовидне наслідування та Геометрична задача.

Завдання 1.

Створіть клас Employee, який має атрибути name та salary.
Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
Клас Manager повинен мати додатковий атрибут department, а клас Developer -
атрибут programming_language.
Тепер створіть клас TeamLead, який успадковується як від Manager,
так і від Developer. Цей клас представляє керівника з команди розробників.
Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ),
а також атрибут team_size, який вказує на кількість розробників у команді,
якою керує керівник.
Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у
класі TeamLead
"""

import math
from abc import ABC, abstractmethod


# Клас Employee
class Employee:
    """Клас Employee з атрибутами name та salary."""

    def __init__(self, name, salary):
        """Ініціалізує працівника з ім'ям та зарплатою."""
        self.name = name
        self.salary = salary


class Manager(Employee):
    """Клас Manager, успадковується від Employee."""

    def __init__(self, name, salary, department):
        """Ініціалізує менеджера з ім'ям, зарплатою та відділом."""
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    """Клас Developer, успадковується від Employee."""

    def __init__(self, name, salary, programming_language):
        """Ініціалізує розробника з ім'ям, зарплатою та мовою програмування."""
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    """Клас TeamLead, успадковується від Manager та Developer."""

    def __init__(
            self, name, salary, department, programming_language, team_size,
    ):
        """Ініціалізує керівника команди."""
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


# Тест для перевірки наявності атрибутів
if __name__ == '__main__':
    # Об'єкт TeamLead
    team_lead = TeamLead('Liuda', 5000, 'Розробка', 'Python', 5)

    # Перевірка атрибутів
    if not hasattr(team_lead, 'name'):
        raise ValueError("Атрибут 'name' відсутній у TeamLead")
    if not hasattr(team_lead, 'salary'):
        raise ValueError("Атрибут 'salary' відсутній у TeamLead")
    if not hasattr(team_lead, 'department'):
        raise ValueError("Атрибут 'department' відсутній у TeamLead")
    if not hasattr(team_lead, 'programming_language'):
        raise ValueError("Атрибут 'programming_language' відсутній у TeamLead")
    if not hasattr(team_lead, 'team_size'):
        raise ValueError("Атрибут 'team_size' відсутній у TeamLead")

    # Виведення інформації для перевірки
    print("Ім'я:", team_lead.name)
    print('Зарплата:', team_lead.salary)
    print('Відділ:', team_lead.department)
    print('Мова програмування:', team_lead.programming_language)
    print('Розмір команди:', team_lead.team_size)

    print('\nУсі атрибути наявні, тест пройдено успішно!')


"""Завдання 2.
Створіть абстрактний клас "Фігура" з абстрактними методами для
отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте
математично вірні для них методи для площі та периметру.
Властивості по типу “довжина сторони” й т.д. повинні бути
приватними, та ініціалізуватись через конструктор.
Створіть Декілька різних об’єктів фігур,
та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""


class Figure(ABC):
    """Абстрактний клас Figure."""

    @abstractmethod
    def get_area(self):
        """Площа."""

    @abstractmethod
    def get_perimeter(self):
        """Периметр."""


class Rectangle(Figure):
    """Клас Rectangle (Прямокутник)."""

    def __init__(self, width, height):
        """Width, height."""
        self.__width = width
        self.__height = height

    def get_area(self):
        """Площа прямокутника."""
        return self.__width * self.__height

    def get_perimeter(self):
        """Периметр трикутника."""
        return 2 * (self.__width + self.__height)


class Circle(Figure):
    """Клас Circle (Коло)."""

    def __init__(self, radius):
        """Ініціалізує коло із заданим радіусом."""
        self.__radius = radius

    def get_area(self):
        """Площа кола."""
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        """Периметр кола."""
        return 2 * math.pi * self.__radius


class Triangle(Figure):
    """Клас Triangle (Трикутник)."""

    def __init__(self, a, b, c):
        """Ініціалізує трикутник."""
        self.__a = a
        self.__b = b
        self.__c = c

    def get_area(self):
        """Площа трикутника."""
        s = (self.__a + self.__b + self.__c) / 2
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

    def get_perimeter(self):
        """Периметр кола."""
        return self.__a + self.__b + self.__c


# Створення об'єктів різних фігур
shapes = [
    Rectangle(4, 5),
    Circle(3),
    Triangle(3, 4, 5),
]

# Цикл для обчислення та виведення площі та периметру кожної фігури
for shape in shapes:
    print(f'Фігура: {shape.__class__.__name__}')
    print(f'Площа: {shape.get_area():.2f}')
    print(f'Периметр: {shape.get_perimeter():.2f}')
    print('-' * 30)
