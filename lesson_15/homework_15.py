"""Створіть клас геометричної фігури 'Ромб'.

Клас повинен мати наступні атрибути:
- сторона_а (довжина сторони a).
- кут_а (кут між сторонами a і b).
- кут_б (суміжний з кутом кут_а).

Вимоги:
1. Значення сторони сторона_а повинно бути більше 0.
2. Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180.
3. При заданому значенні кут_а, значення кут_б обчислюється автоматично.
4. Для встановлення значень атрибутів використовуйте метод __setattr__.
"""


class Rhombus:
    """Клас фігури 'Ромб' з атрибутами side_a, angle_a та angle_b."""

    def __init__(self, side_a, angle_a):
        """Ініціалізація атрибутів сторони та кутів."""
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = 180 - angle_a
# Ініціалізація angle_b під час створення об'єкта

    def __setattr__(self, name, value):
        """Перевизначений метод для встановлення атрибутів."""
        if name == 'side_a':
            if value <= 0:
                raise ValueError("Сторона 'side_a' повинна бути більше 0.")
        elif name == 'angle_a':
            if not 0 < value < 180:
                raise ValueError(
                    "Кут 'angle_a' в діапазоні від 0 до 180 градусів.",
                )
            # Автоматично обчислюємо суміжний кут
            object.__setattr__(self, 'angle_b', 180 - value)

        # Встановлення значення атрибуту
        object.__setattr__(self, name, value)

    def __repr__(self):
        """Повернення строкового представлення об'єкта ромба."""
        return (
            f'Rhombus(side_a={self.side_a}, '
            f'angle_a={self.angle_a}, '
            f'angle_b={self.angle_b})'
        )


# Створення об'єкта ромба з коректними параметрами
try:
    rhombus1 = Rhombus(5, 60)
    print(rhombus1)  # Rhombus(side_a=5, angle_a=60, angle_b=120)

# Створити ромб з некоректною стороною
    rhombus2 = Rhombus(-3, 60)
except ValueError as e:
    print(f'Помилка: {e}')

# Створення ромб з некоректним кутом
try:
    rhombus3 = Rhombus(4, 190)
except ValueError as e:
    print(f'Помилка: {e}')
