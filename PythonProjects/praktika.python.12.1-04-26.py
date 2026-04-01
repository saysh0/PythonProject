#task1 Сумма чисел списка.
# Напишите рекурсивную функцию, которая вычисляет сумму всех чисел в списке.
# Функция должна проверять:
# Аргумент должен быть списком.
# Все элементы списка должны быть числами.
# Если данные не валидны необходимо выбрасывать исключение. При вызове функции обработайте
# возможное исключение.
# Данные
# numbers = [1, 2, 3, 4, 5]
# Пример вывода
# 15
from collections import defaultdict

numbers = [1, 2, 3, 4, 5]
def sum_numbers(num):
    if not isinstance(num, list):
        raise TypeError('num must be a list')
    for i in num:
        if not isinstance(i, int):
            raise TypeError('num must be a int')
        return num[0] + sum_numbers(num[1:])
    return 0
print(sum_numbers(numbers))

#task2 Реверс строки.
# Напишите рекурсивную функцию, которая переворачивает строку. Если передан не строковый тип, выбросить
# исключение. При вызове функции обработайте возможное исключение.
# Данные
# text = "recursion"
# Пример вывода
# noisrucer

text = "recursion"
def reverse_string(s):
    if not isinstance(s, str):
        raise TypeError('s must be a string')
    if s:
        print(s)
        return s[-1] + reverse_string(s[:-1])
    else:
        return ''
print(reverse_string(text))

#task3 Реверс строки.
# Глубина вложенности списка
# Напишите рекурсивную функцию, которая определяет максимальную глубину вложенности списка. Функция
# должна проверять:
# ● Аргумент должен быть списком.
# ● Вложенные структуры, если они есть, также должны быть списками.
# Если данные не валидны необходимо выбрасывать исключение. При вызове функции обработайте
# возможное исключение.
# Данные
# nested_list = [1, [2, [3, [4, [5]]]], 6, [[7, 8], 9]]
# Пример вывода
# Максимальная глубина: 5

nested_list = [1, [2, [3, [4, [5]]]], 6, [[7, 8], 9]]
def msx_dep_list(lst):
    if not isinstance(lst, list):
        raise TypeError('s must be a list')
    for i in lst:
        if isinstance(i, list):
            return 1 + msx_dep_list(i)
    return 1
print(msx_dep_list(nested_list))

#task4 Сумма продаж.
# Есть дерево подразделений внутри компании (каждое подразделение может содержать «дочерние» отделы).
# Напишите рекурсивную функцию, которая подсчитывает суммарные продажи для всех отделов. Функция должна
# проверять:
# ● Аргумент должен быть словарем.
# ● Дочерние отделы (если есть) должны быть списком словарей.
# Если данные не валидны необходимо выбрасывать исключение. При вызове функции обработайте
# возможное исключение.
# Пример вывода
# Общая сумма продаж: 1140

company_structure = {
    "dept_name": "Head Office",
    "sales": 100,
    "sub_departments": [
        {
            "dept_name": "Sales Department",
            "sales": 200,
            "sub_departments": [
                {
                    "dept_name": "B2B Sales",
                    "sales": 120,
                }
            ]
        },
        {
            "dept_name": "IT Department",
            "sales": 150,
            "sub_departments": [
                {
                    "dept_name": "DevOps",
                    "sales": 300,
                    "sub_departments": [
                        {
                            "dept_name": "Cloud Infrastructure",
                            "sales": 180,
                        }
                    ]
                }
            ]
        },
        {
            "dept_name": "QA Department",
            "sales": 90,
        }
    ]
}
def sale_sum(dit):
    if not isinstance(dit, dict):
        raise TypeError('dit must be a dict')
    res = dit.get('sale', 0)
    for department in dit.get('sub_departments', []):
        res += sale_sum(department)
    return res
print(sale_sum(company_structure))

def sale_sum(dit):
    d = defaultdict(int, dit)
    res = d['sales']
    for department in dit.get('sub_departments', []):
        res += sale_sum(department)
    return res
print(sale_sum(company_structure))

#task5 Читабельный формат словаря.
# Дан вложенный словарь. Напишите рекурсивную функцию, которая преобразует его в «плоский» формат,
# где в ключе будет содержаться полный путь к значению.
# Пример вывода
# Данные для анализа:
# user.id : 123
# user.info.name : Alice
# user.info.location.city : Berlin
# user.info.location.coordinates.lat : 52.52
# user.info.location.coordinates.lon : 13.405
# user.info.hobby : ['swimming', 'drawing']
# score : 95

data = {
    "user": {
        "id": 123,
        "info": {
            "name": "Alice",
            "location": {
                "city": "Berlin",
                "coordinates": {
                    "lat": 52.52, "lon": 13.405}
            },
            "hobby": ["swimming", "drawing"]
        }
    },
    "score": 95
}
def translate_dict(d, p = ''):
    res = {}
    for k, v in d.items():
        key = f'{p}.{k}' if p else k
        if isinstance(v, dict):
            res.update(translate_dict(v, key))
        else:
            res[key] = v
    return res
for k1, v1 in translate_dict(data).items():
    print(f'{k1} : {v1}')



