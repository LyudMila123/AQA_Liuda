"""Homework 6.3. Сумуємо числа."""

# Є ліст з числами,
# порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
numbers_sum = sum(item for item in numbers if item % 2 == 0)
print(numbers_sum)
