#task1 Фильтрация по ключевому слову.
# Напишите программу, которая ищет в файле все строки, содержащие указанное пользователем слово, и сохраняет их в новый файл.
# Имя нового файла формируется как <keyword>_<original_filename>.
# Если файл не существует, программа должна вывести ошибку.
# Если совпадения не найдены, новый файл не создаётся.
# Используйте файл system_log.txt.
# Пример ввода:
# Введите имя файла для поиска: system_log.txt
# Введите ключевое слово: error
# Пример вывода:
# Строки, содержащие 'error', сохранены в error_system_log.txt.

import os
target_file_name = input('Введите имя файла для поиска: ')
target_word = input('Введите ключевое слово: ')
if not os.path.exists(target_file_name):
    print(f"Ошибка: Файл '{target_file_name}' не найден.")
else:
    name_to_create_file = f'{target_word}_{target_file_name}'
    target_lines = []
    with open(target_file_name, mode='r', encoding="utf-8") as f:
        for line in f:
            if target_word.lower() in line.lower():
                target_lines.append(line)
    if target_lines:
        with open(name_to_create_file, mode='w', encoding="utf-8") as fa:
            fa.writelines(target_lines)
        print(f'Строки, содержащие "{target_word}", сохранены в {name_to_create_file}.')
    else:
        print(f'Нет строк, содержащих "{target_word}" в файле {target_file_name}, файл не был создан.')


#task2 Поиск и удаление дубликатов.
# Напишите программу, которая удаляет дублирующиеся строки из файла и сохраняет результат в новый файл.
# Имя нового файла формируется как unique_<original_filename>.
# Если файл не существует, программа должна вывести ошибку.
# Исходный порядок строк должен сохраниться.
# Если в файле нет дубликатов, создаётся точная копия файла.
# Используйте файл movies_to_watch.txt.
# Пример ввода:
# Введите имя файла: movies_to_watch.txt
# Пример вывода:
# Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.

target_file_name = input("Введите имя файла: ")
if not os.path.exists(target_file_name):
    print(f"Ошибка: Файл '{target_file_name}' не найден.")
else:
    with open(target_file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    unique_lines_set = set()
    unique_lines = []
    for line in lines:
        if line not in unique_lines_set:
            unique_lines.append(line)
            unique_lines_set.add(line)
    new_filename = f"unique_{target_file_name}"
    with open(new_filename, 'w', encoding='utf-8') as f:
        f.writelines(unique_lines)
    print(f"Дубликаты удалены. Уникальные строки сохранены в {new_filename}.")

