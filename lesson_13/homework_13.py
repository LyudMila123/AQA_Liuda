"""Модуль для обробки CSV, JSON і XML файлів."""

import csv
import json
import logging
from pathlib import Path

from defusedxml import ElementTree

# Завдання 1
# Візьміть два файли з теки ideas_for_test/work_with_csv порівняйте на
# наявність дублікатів і приберіть їх.
# Результат запишіть у файл result_<your_second_name>.csv

# Шляхи до файлів
base_dir = Path(
    '/Users/ac/automation/pythonProject1/AQA_Liuda/lesson_13/work_with_csv',
)
file1_path = base_dir / 'r-m-c.csv'
file2_path = base_dir / 'random-michaels.csv'

# Збереження результату
result_path = base_dir.parent / 'result_Chunikhina.csv'

# Зчитуємо дані з обох файлів та видаляємо дублікати
unique_rows = set()

for file_path in [file1_path, file2_path]:
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            unique_rows.add(tuple(row))

# Записуємо унікальні рядки у файл з результатом
with open(result_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(unique_rows)

print(f'Результат збережено у файл: {result_path.resolve()}')

# Завдання 2
# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json
# є валідними json.

# Шлях до папки з JSON-файлами
base_dir = Path(
    '/Users/ac/automation/pythonProject1/AQA_Liuda/lesson_13/work_with_json',
)

# Налаштування логера
logging.basicConfig(filename='json_Chunikhina.log', level=logging.ERROR)

# Перевірка всіх JSON-файлів у папці
for file in base_dir.glob('*.json'):
    try:
        with open(file, encoding='utf-8') as f:
            json.load(f)
        print(f'{file.name} - valid JSON')
    except json.JSONDecodeError:
        logging.error('%s - NOT valid JSON', file.name)
        print(f'{file.name} - NOT valid JSON')

# Завдання 3
# Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку
# по group/number.

# Налаштування логера для виведення у консоль
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

# Шлях до XML-файлу
xml_file_path = Path(
    '/Users/ac/automation/pythonProject1/AQA_Liuda/lesson_13/groups.xml',
)


def find_timing_incoming(group_number):
    """Шукає значення timingExbytes/incoming за group/number."""
    try:
        if not xml_file_path.exists():
            logging.error('Файл %s не знайдено.', xml_file_path)
            return None

        tree = ElementTree.parse(xml_file_path)
        root = tree.getroot()

        for group in root.findall('.//group'):
            if group.findtext('number') == group_number:
                timing = group.findtext('.//timingExbytes/incoming')
                if timing:
                    logging.info('Знайдено timingExbytes/incoming: %s', timing)
                    return timing

        logging.info('group/number %s не знайдено.', group_number)
    except ElementTree.ParseError as e:
        logging.error('Помилка парсингу XML: %s', e)
    except IOError as e:
        logging.error('Помилка вводу/виводу: %s', e)

    return None


# Виклик функції для конкретного номера групи
GROUP_NUMBER_TO_FIND = '2'  # Можна замінити на інший номер групи
result = find_timing_incoming(GROUP_NUMBER_TO_FIND)

if result:
    print(f'Результат: {result}')
else:
    print('Дані не знайдено.')

GROUP_NUMBER_TO_FIND = input('Введіть номер групи для пошуку: ').strip()
result = find_timing_incoming(GROUP_NUMBER_TO_FIND)

if result:
    print(f'Результат: {result}')
else:
    print('Дані не знайдено.')
