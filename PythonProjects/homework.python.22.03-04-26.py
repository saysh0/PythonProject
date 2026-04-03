#task1 Выбор заказов.
# У вас есть список заказов. Каждый заказ содержит название продукта и его цену.
# Напишите функцию, которая:
# Отбирает заказы дороже 500.
# Создаёт список названий отобранных продуктов в алфавитном порядке.
# Возвращает итоговый список названий.
# Данные:
# orders = [
#
#     {"product": "Laptop", "price": 1200},
#
#     {"product": "Mouse", "price": 50},
#
#     {"product": "Keyboard", "price": 100},
#
#     {"product": "Monitor", "price": 300},
#
#     {"product": "Chair", "price": 800},
#
#     {"product": "Desk", "price": 400}
# ]
# Пример вывода:
# ['Chair', 'Laptop']

orders = [

    {"product": "Laptop", "price": 1200},

    {"product": "Mouse", "price": 50},

    {"product": "Keyboard", "price": 100},

    {"product": "Monitor", "price": 300},

    {"product": "Chair", "price": 800},

    {"product": "Desk", "price": 400}
]
def order_chose(order):
    filtered = filter(lambda x: x["price"] > 500, order)
    res = map(lambda x: x["product"], filtered)
    return list(res)
print(order_chose(orders))

#task2 Статистика продаж.
# Дан список продаж в виде кортежей (товар, количество, цена).
# Напишите программу, которая:
# Вычисляет общую выручку для каждого товара.
# Возвращает словарь с товарами {товар: выручка}, отсортированный по убыванию выручки.
# Данные:
# sales = [
#     ("Laptop", 5, 1200),
#
#     ("Mouse", 50, 20),
#
#     ("Keyboard", 30, 50),
#
#     ("Monitor", 10, 300),
#
#     ("Chair", 20, 800)
# ]
# Пример вывода:
# {'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}

sales = [
    ("Laptop", 5, 1200),

    ("Mouse", 50, 20),

    ("Keyboard", 30, 50),

    ("Monitor", 10, 300),

    ("Chair", 20, 800)
]
def sale_status(sale):
    profit = [(item[0], item[1] * item[2]) for item in sale]
    sorted_sales = sorted(profit, key=lambda x: x[1], reverse=True)
    complete_dict = dict(sorted_sales)
    return complete_dict
print(sale_status(sales))