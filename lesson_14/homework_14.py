"""Створіть клас 'Студент'.

З атрибутами 'імʼя', 'прізвище', 'вік' та 'середній бал'.
Створіть об'єкт цього класу, представляючи студента.
Потім додайте метод до класу 'Студент', який дозволяє змінювати
середній бал студента. Виведіть інформацію про студента та змініть
його середній бал.
"""


class Student:
    """Клас з атрибутами імʼя, прізвище, вік та середній бал."""

    def __init__(self, first_name, last_name, age, average_grade):
        """Ініціалізує атрибути студента."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def update_average_grade(self, new_grade):
        """Оновлює середній бал студента."""
        self.average_grade = new_grade

    def info(self):
        """Виводить інформацію про студента."""
        print(f'First name: {self.first_name}')
        print(f'Last name: {self.last_name}')
        print(f'Age: {self.age}')
        print(f'Average grade: {self.average_grade}')


# Створення об'єкта студента
student_a = Student('Liuda', 'Chunikhina', 37, 4.0)

print('Info about student before changing the average grade:')
student_a.info()

# Новий середній бал
student_a.update_average_grade(5.5)

print('\nInfo about student after changing the average grade:')
student_a.info()
