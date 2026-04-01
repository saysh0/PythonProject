#task1
num = int(input('Введите число: '))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f'Факториал числа {num} равен {factorial}')
#task2
num = int(input('Введите ширину: '))
num1 = int(input('Введите высоту: '))
for i in range(num1):
    for j in range(num):
        print('*', end='')
    print()
#task3
num = int(input('Введите число: '))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Не является простым")
            break
    else:
        print("Является простым")
else:
    print("Не является простым")