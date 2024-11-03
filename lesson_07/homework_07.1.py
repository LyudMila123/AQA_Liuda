# task 1
r"""Задача.

надрукувати табличку множення на задане число,
але лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки
та випраавити\доповнити.
"""


def multiplication_table(number):
    """Initialize the appropriate variable."""
    multiplier = 1
    # Complete the while loop condition.
    while True:
        result = number * multiplier
        if result > 25:
            break
            # Enter the action to take if the result is greater than 25
        print(str(number) + 'x' + str(multiplier) + '=' + str(result))
        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def sum_two_numbers(a, b):
    """Sum for two numbers."""
    return a + b


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def calculate_numbers(numbers):
    """Середнє арифметичне."""
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return 0


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reverse_string(a):
    """Return str."""
    return a[::-1]


# task 5
"""  Написати функцію, яка приймає список слів та повертає
найдовше слово у списку.
"""


def longest_word(words):
    """Longest word."""
    if words:
        return max(words, key=len)
    else:
        return ''


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс
першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка,
та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    """Возвращает индекс первого вхождения подстроки в строке или -1."""
    return str1.find(str2)


str1 = 'Hello, world!'
str2 = 'world'
print(find_substring(str1, str2))  # поверне 7


str1 = 'The quick brown fox jumps over the lazy dog'
str2 = 'cat'
print(find_substring(str1, str2))  # поверне -1


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
"""Task from 6.4"""
# Є ліст з числами,
# порахуйте сумму усіх ПАРНИХ чисел в цьому лісті


def numbers_sum(numbers):
    """Рахуємо суму усіх парних чисел в цьому лісті."""
    return sum(item for item in numbers if item % 2 == 0)


# task 8
"""Task from 6.3."""
# Є list з даними
# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0,
# 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2),
# який містить лише змінні
# типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими


def new_strings(lst1):
    """Новий список, де лише str."""
    return [item for item in lst1 if isinstance(item, str)]


# task 9
"""Task from 6.2."""

# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому
# є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".


def word_h():
    """Ввод слово з буквою h."""
    while True:
        word = input("Введіть слово, що містить букву 'h': ")
        if 'h' in word.h.lower():
            print("Супер! Слово з буквою 'h'.")
            return word
        else:
            print("Упс! В слові немає букви 'h'.")


# task 10
"""Task from 6.1."""

# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()
# Отримати строку від користувача


def more_ten_unique_symbols(input_string):
    """Перевірка, чи містить строка 10 унікальних символів."""
    unique_symbols = len(set(input_string))
    return unique_symbols > 10
