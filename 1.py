# Задача 1. Язык математики
a = 8
b = 10
c = 12
d = 18

res = (a + b) / c * d
print("Задача 1. Результат:", res)

# Задача 2. Финансовый отчёт
q1 = float(input("Задача 2. Введите доход за первый квартал: "))
q2 = float(input("Введите доход за второй квартал: "))
q3 = float(input("Введите доход за третий квартал: "))
q4 = float(input("Введите доход за четвертый квартал: "))

sum_first_half = q1 + q2
sum_second_half = q3 + q4

result = sum_first_half / sum_second_half
print("Результат:", result)

# Задача 3. Следующее и предыдущее числа
num = int(input("Задача 3. Введите число: "))
print("Следующее число:", num + 1)
print("Предыдущее число:", num - 1)

# Задача 4. Площадь треугольника
a = float(input("Задача 4. Введите длину первого катета: "))
b = float(input("Введите длину второго катета: "))

s = (a * b) / 2
print("Площадь треугольника:", s)

# Задача 5. Часы
minutes = int(input("Задача 5. Введите количество минут: "))
hours = minutes // 60
remaining_minutes = minutes % 60

print(f"{minutes} минут - это {hours} часов и {remaining_minutes} минут.")

# Задача 6. Проверяем бухгалтера
num1 = int(input("Задача 6. Введите первое число: "))
num2 = int(input("Введите второе число: "))

last_two_digits1 = num1 % 100
last_two_digits2 = num2 % 100

result = last_two_digits1 + last_two_digits2
print("Сумма двух последних цифр:", result)

# Задача 7. Режем число на части
number = int(input("Задача 7. Введите четырёхзначное число: "))

digit1 = number // 1000
digit2 = (number // 100) % 10
digit3 = (number // 10) % 10
digit4 = number % 10

print(digit1, digit2, digit3, digit4)

# Задача 8. Поменять местами: не всё так просто!
a = int(input('Задача 8. Введите первое число: '))
b = int(input('Введите второе число: '))

a = a + b
b = a - b
a = a - b

print(a, b)