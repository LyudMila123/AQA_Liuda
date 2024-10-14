"""Homework 1."""

# task 01 == Виправте синтаксичні помилки
print('Hello', end=' ')
print('world!')

# task 02 == Виправте синтаксичні помилки
hello = 'Hello'
world = 'world'
print(hello, world)

# task 03  == Вcтавте пропущену змінну у ф-цію print
for boost in 'Hello world!':
    print(boost)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
bananas = apples * 4

# task 05 == Виправте назви змінних
side_one = 1
side_two = 2
side_three = 3
side_four = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = side_one + side_two + side_three + side_four
print(perimetery)


# Задачі 07 - 10:
# Переведіть задачі з книги "Математика, 2 класc.
# на мову пітон і виведіть відповідь, так, щоб було зрозуміло дитині
# що навчається в другому класі

# task 07
# У саду посадили 4 яблуні.
# Груш на 5 більше яблунь, а слив - на 2 менше.
# Скільки всього дерев посадили в саду?

apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2
trees = apple_trees + pear_trees + plum_trees
print('Всього посадили', trees, 'дерев в саду')


# task 08
# До обіда температура повітря була на 5 градусів вище нуля.
# Після обіду температура опустилася на 10 градусів.
# Надвечір потепліло на 4 градуси. Яка температура надвечір?

temperature_before_lunch = 5
temperature_after_lunch = temperature_before_lunch - 10
temperature_in_evening = temperature_after_lunch + 4
print('Температура надвечір становить', temperature_in_evening, 'градусів')


# task 09
# Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
# 1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
# Скільки сьогодні дітей у театральному гуртку?

boys = 24
girls = boys // 2
boys_today = boys - 1
girls_today = girls - 2
children_today = boys_today + girls_today
print('Сьогодні у театральному кружку', children_today, 'дітей')


# task 10
# Перша книжка коштує 8 грн., друга - на 2 грн.
# Дороже, друзьям - як половина вартості першої та другої разом.
# Скільки будуть коштувати усі книги, якщо купити по одному примірнику.

price_first_book = 8
price_second_book = price_first_book + 2
price_third_book = (price_first_book + price_second_book) / 2
price_all_books = price_first_book + price_second_book + price_third_book
print('Вартість книжок становить', price_all_books, 'грн')
