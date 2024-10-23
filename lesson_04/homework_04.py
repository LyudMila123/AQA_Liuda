"""Робота зі строками."""

import re

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by,
dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance
to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

#  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином,
через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer_space_end = adwentures_of_tom_sawer.replace('\n', ' ')


print(adwentures_of_tom_sawer_space_end)

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer_spac = adwentures_of_tom_sawer.replace('...', '')
print(adwentures_of_tom_sawer_spac)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами."""
adwentures_of_tom_sawer_one_spac = re.sub(r'\s+', ' ', adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer_one_spac)


# task 04
"""Виведіть, скількі разів у тексті зустрічається літера 'h"""
count_h = adwentures_of_tom_sawer.count('h')
print(f"Кількість літери 'h' у тексті: {count_h}")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?"""
capitalized_words = re.findall(r'\b[A-Z][a-z]*', adwentures_of_tom_sawer)
print(f'Кількість слів з великої літери: {len(capitalized_words)}')

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге"""
position_first = adwentures_of_tom_sawer.find('Tom')
position_second = adwentures_of_tom_sawer.find('Tom', position_first + 1)
print(f'Позиція, на якій слово Tom зустрічається вдруге: {position_second}')

# task 07
"""Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences"""
# Розбиваємо текст по кінцю речення після ".", "!" або "?"

adwentures_of_tom_sawer_sentance = re.split(
    r'(?<=[.!?])\s+', adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer_sentance)

# task 08
"""Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр."""
# Ділимо текст на речення
adwentures_of_tom_sawer_sentences = re.split(
    r'[.!?]\s+', adwentures_of_tom_sawer)

# Перевіряємо, що 4 речення або більше
if len(adwentures_of_tom_sawer_sentences) >= 4:
    # Отримуємо четверте речення (індексація починається з 0) і перетворюємо
    # його в нижній регістр
    sentence_fourth = adwentures_of_tom_sawer_sentences[3].lower()
    print(sentence_fourth)
else:
    print('Четвертого речення немає.')

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
adwentures_of_tom_sawer_sentences = re.split(r'[.!?]\s+',
                                             adwentures_of_tom_sawer)

# Перевіряємо, чи є речення, що починається з "By the time"
found = False
for sentence_by_the_time in adwentures_of_tom_sawer_sentences:
    if sentence_by_the_time.startswith('By the time'):
        found = True
        print(f'Речення починається з "By the time": {sentence_by_the_time}')
        break

if not found:
    print('Немає речення, що починається з "By the time".')

# task 10
"""Виведіть кількість слів останнього
речення з adwentures_of_tom_sawer_sentences."""
adwentures_of_tom_sawer_sentences = re.split(r'[.!?]\s+',
                                             adwentures_of_tom_sawer)

# Щоб отримати останнє речення
last_sentence = adwentures_of_tom_sawer_sentences[-1]

# Розбити речення на слова
words_last_sentence = last_sentence.split()

# Кількість слів в останньому реченні
print(f'Кількість слів в останньому реченні: {len(words_last_sentence)}')
