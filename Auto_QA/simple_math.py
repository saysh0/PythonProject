# Класс для задания.
# Создайте файл simple_math. ру и напишите в нём следующий класс:
class SimpleMath:
    def square(self, x):
        return x * x

    def cube(self, x):
        return x * x * x
# Задание
# 1. Цель: Написать юнит-тесты для класса SimpleMath.
# 2. Инструкция:
# Создайте файл test_simple_math.py.
# Напишите в нём тесты для методов square и cube.
# Проверьте корректность работы методов для разных входных значений (например, положительных, отрицательных и нуля).
# Пример ожидаемого поведения:
# Метод square (2) должен возвращать 4.
# Метод cube(-3) должен возвращать -27.
# В качестве ответа приложить ссылку на репозиторий в git.

math = SimpleMath()
#test square
res = math.square(5)
assert res == 25

res = math.square(-5)
assert res == 25

res = math.square(0)
assert res == 0

res = math.square(-0)
assert res == 0

res = math.square(5.5)
assert res == 30.25

res = math.square(-5.5)
assert res == 30.25

#task cube
res = math.cube(5)
assert res == 125

res = math.cube(-5)
assert res == -125

res = math.cube(0)
assert res == 0

res = math.cube(-0)
assert res == -0

res = math.cube(5.5)
assert res == 166.375

res = math.cube(-5.5)
assert res == -166.375