"""Модуль для задач с использованием строк и математических вычислений.""
# task 01 == Розділіть alice_in_wonderland, щоб вона займала декілька фіз.лінії
alice_in_wonderland = (
    "'Would you tell me, please,"
    " which way I ought to go from here?'\n"
    "'That depends a good deal on where you want to get to,' said the Cat.\n"
    "'I don’t much care where ——' said Alice.\n"
    "'Then it doesn’t matter which way you go,' said the Cat.\n"
    "'—— so long as I get somewhere,' Alice added as an explanation.\n"
    "'Oh, you’re sure to do that,' said the Cat,"
    "'if you only walk long enough.'"
)

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
single_quotes = [char for char in alice_in_wonderland if char == "'"]
print('Одинарні лапки: ', single_quotes)
print(f'Всього знайдено {len(single_quotes)} одинарних лапок.')

# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
plosha_chornogo_morya = 436402  # км²
plosha_azovskogo_morya = 37800  # км²

zaghalna_plosha = plosha_chornogo_morya + plosha_azovskogo_morya
print(
    f'Загальна площа Чорного та Азовського морів разом становить '
    f'{zaghalna_plosha} км².',
)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

s1_plus_s2 = 250449
s2_plus_s3 = 222950
s1_plus_s2_plus_s3 = 375291

s1 = s1_plus_s2_plus_s3 - s2_plus_s3  # Количество товаров на первом складе
s3 = s1_plus_s2_plus_s3 - s1_plus_s2  # Количество товаров на третьем складе
s2 = s1_plus_s2 - s1                  # Количество товаров на втором складе

print(f'На першому складі розміщено {s1} товарів.')
print(f'На другому складі розміщено {s2} товарів.')
print(f'На третьому складі розміщено {s3} товарів.')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
payment_per_month = 1179  # грн/місяць
months = 1.5 * 12  # 1.5 року = 18 місяців

total_cost = payment_per_month * months
print(
    f"Вартість комп\'ютера становить {total_cost} грн.")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print(f'Остача від ділення 8019 на 8: {a}')
print(f'Остача від ділення 9907 на 9: {b}')
print(f'Остача від ділення 2789 на 5: {c}')
print(f'Остача від ділення 7248 на 6: {d}')
print(f'Остача від ділення 7128 на 5: {e}')
print(f'Остача від ділення 19224 на 9: {f}')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_big_quantity = 4
pizza_big_price = 274

pizza_medium_quantity = 2
pizza_medium_price = 218

juice_quantity = 4
juice_price = 35

cake_quantity = 1
cake_price = 350

water_quantity = 3
water_price = 21

total_pizza_big = pizza_big_quantity * pizza_big_price
total_pizza_medium = pizza_medium_quantity * pizza_medium_price
total_juice = juice_quantity * juice_price
total_cake = cake_quantity * cake_price
total_water = water_quantity * water_price

total_cost = (
    total_pizza_big + total_pizza_medium + total_juice + total_cake +
    + total_water
)
print(f'Загальна сума для замовлення Іринки: {total_cost} грн.')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photos = 232  # Загальна кількість фотографій
photos_per_page = 8  # Кількість фотографій на одній сторінці

pages_needed = (
    (total_photos + photos_per_page - 1) // photos_per_page
)
# округлення в більшу сторону
print(f'Ігорю знадобиться {pages_needed} сторінок, щоб вклеїти всі фото.')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance_km = 1600  # Відстань між Харковом і Будапештом, км
fuel_per_100_km = 9  # Витрата бензину на 100 км, літрів
tank_capacity = 48  # Місткість баку, літрів

total_fuel_needed = (distance_km / 100) * fuel_per_100_km
refuels_needed = total_fuel_needed / tank_capacity
refuels_needed = (int(refuels_needed) if refuels_needed.is_integer()
                  else int(refuels_needed) + 1)

print(
    f'Для подорожі знадобиться {total_fuel_needed} літрів бензину.',
)
print(
    f'Щонайменше {refuels_needed} разів потрібно буде заїхати на заправку.',
)
