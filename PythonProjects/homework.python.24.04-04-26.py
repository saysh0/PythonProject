#task1 Сумма цифр числа.
# Напишите рекурсивную функцию, которая находит сумму всех цифр числа.
# Данные:
# num = 43197
# Пример вывода:
# 24

num = 43197
def sum_numbers(n):
    if n == 0:
        return 0
    return n % 10 + sum_numbers(n // 10)
print(sum_numbers(num))

#task2 Сумма вложенных чисел.
# Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.
# Данные:
# nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
# Пример вывода:
# 28

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
# def sum_num_in_list(n):
#     res = 0
#     for i in n:
#         if isinstance(i, list):
#             res += sum_num_in_list(i)
#         else:
#             res += i
#     return res
# print(sum_num_in_list(nested_numbers))

def sum_num1(n):
    return sum([sum_num1(i) if isinstance(i,list) else i for i in n])
print(sum_num1(nested_numbers))



