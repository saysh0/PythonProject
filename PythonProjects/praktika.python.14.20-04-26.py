#task1 Генератор, аналогичный range()
# Создайте генератор, который повторяет функциональность range(),
# принимая start, stop, step и возвращая последовательность чисел.
# Данные:
# start = 2
# stop = 10
# step = 2
# Пример вывода:
# 2
# 4
# 6
# 8

# start = 10
# stop = 2
# step = -2
# def copy_range(start, stop, step=1):
#     if step == 0:
#         raise ValueError('Ай ай ай')
#     if step > 0:
#         while start < stop:
#             yield start
#             start += step
#     else:
#         while start > stop:
#             yield start
#             start += step
#
#
# for i in copy_range(start, stop, step):
#     print(i)

#task2 Генератор случайных дат
# Создайте генератор, который генерирует случайные даты в пределах одного года.
# Генератор должен принимать год в качестве аргумента и выдавать следующую случайную дату при каждом
# вызове, учитывая количество дней в месяце, а также високосные годы.
# Пример вывода:
# 2025-02-14
# 2025-06-28
# 2025-09-09

import random
# def date_generate(year):
#     m_2 = 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28
#     months = {1: 31, 2: m_2, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
#     while True:
#         rnd_month = random.randint(1, 12)
#         rnd_day = random.randint(1, months[rnd_month])
#         yield f"{year}-{rnd_month:02d}-{rnd_day:02d}"
#
#
# gen = date_generate(2025)
# for i in range(10):
#     print(next(gen))

#task3 Генератор случайных имён
# Создайте генератор, который выдаёт случайные имена и фамилии.
# Выведите 5 имён.
# Для получения случайного значения из списка можно использовать choice() из модуля random.
# Данные:
# first_names = ["Alice", "Bob", "Charlie", "David", "Emma"]
# last_names = ["Smith", "Johnson", "Brown", "Williams", "Jones"]
# Пример вывода:
# Alice Johnson
# David Brown

# import random
# first_names = ["Alice", "Bob", "Charlie", "David", "Emma"]
# last_names = ["Smith", "Johnson", "Brown", "Williams", "Jones"]
# def random_name(f_names, l_names):
#     while True:
#         first = random.choice(f_names)
#         last = random.choice(l_names)
#         yield f"{first} {last}"
#
# gen = random_name(first_names, last_names)
# for i in range(5):
#     print(next(gen))

#task4 Генератор тестовых данных
# Создайте генератор, который принимает список других генераторов и возвращает кортежи, состоящие из значений, полученных от каждого из них.
# Используйте ранее написанные генераторы дат и имён для создания тестовых данных.
# Данные:
# name_gen = random_names()
# date_gen = random_dates(2025)
# Пример вывода:
# ('Emma Brown', 2025-02-14)
# ('Bob Williams', '2025-06-28)
# ('Charlie Johnson', 2025-09-09)

# def gen_text_data(*funcs):
#     while True:
#       yield tuple(next(func) for func in funcs)
#
#
# gen_date = date_generate(2025)
# gen_name = random_name(first_names, last_names)
# for i, data in enumerate(gen_text_data(gen_name, gen_date)):
#     if i == 10:
#         break
#     print(i, data)

#task5 Программа будет состоять из двух частей, работающих независимо:
# ● Добавление задач – пользователь вводит новые задачи, и они записываются в файл.
# ● Распределение задач – другая программа читает задачи из файла и назначает их сотрудникам по
# очереди.
# Запустите обе программы одновременно.

#task5.1 Добавление задач
# Эта программа запрашивает задачи у пользователя и записывает их в файл tasks.txt. Она работает в
# бесконечном цикле, пока пользователь не введёт exit.
# Данные:
# Файл tasks.txt – каждая строка
# содержит одно задание.
# Пример файла:
# Подготовить отчёт
# Провести собрание
# Проверить документацию
# Разработать новый модуль
# Настроить сервер
# Пример вывода:
# Введите задачу: Подготовить отчёт
# Введите задачу: Провести собрание
# Введите задачу: Проверить документацию
# Введите задачу: Разработать новый модуль
# Введите задачу: Настроить сервер
# Введите задачу: exit

# with open('tasksss.txt', 'a', encoding='utf-8') as tasks_file:
#     while True:
#         user_task_input = input('Введите задачу: ')
#         if user_task_input == 'exit':
#             break
#         else:
#             tasks_file.write(user_task_input + '\n')

#task5.2 Распределение задач
# Эта программа читает файл tasks.txt и назначает задачи сотрудникам по очереди.
# Она использует генератор для постепенного чтения новых задач и назначения сотрудникам.
# Дополнительно: если файл tasks.txt отсутствует, программа делает 5 попыток с паузой 3 секунды перед
# завершением.
# Данные:
# employees = ["Alice", "Bob", "Charlie"]
# Пример вывода:
# Alice выполняет: Подготовить отчёт
# Bob выполняет: Провести собрание
# Charlie выполняет: поверить документацию
# Alice выполняет: Разработать новый модуль
# Bob выполняет: Настроить сервер

import itertools
employees = ["Alice", "Bob", "Charlie"]
with open('tasksss.txt', 'r', encoding='utf-8') as f:
