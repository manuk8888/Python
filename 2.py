# Задача 1. Датчик погоды
def weather_sensor():
    rain = int(input("На улице идёт дождь? (1 - да, 0 - нет): "))
    if rain == 1:
        print("Пошёл дождь. Возьмите зонтик!")
    else:
        print("Дождя нет!")

# Задача 2. Поступление
def admission():
    russian = int(input("Введите количество баллов по русскому языку: "))
    math = int(input("Введите количество баллов по математике: "))
    computer_science = int(input("Введите количество баллов по информатике: "))
    total = russian + math + computer_science
    if total >= 270:
        print("Поздравляю, ты поступил на бюджет!")
    else:
        print("К сожалению, ты не прошёл на бюджет.")

# Задача 3. Следим за расписанием
def schedule():
    day = int(input("Введите число: "))
    if day % 2 == 0:
        print("Это чётное число. Рабочий день.")
    else:
        print("Это нечётное число. Выходной.")

# Задача 4. Калькулятор скидки
def discount_calculator():
    price1 = int(input("Введите стоимость первого стула: "))
    price2 = int(input("Введите стоимость второго стула: "))
    price3 = int(input("Введите стоимость третьего стула: "))
    total = price1 + price2 + price3
    if total > 10000:
        total -= total * 0.1
    print(f"Итоговая сумма: {total} руб.")

# Задача 5. Модуль числа
def absolute_value():
    x = int(input("Введите число: "))
    if x < 0:
        x = -x
    print(f"Модуль числа: {x}")

# Задача 6. Игра в кубики
def dice_game():
    player = int(input("Кубик Кости: "))
    owner = int(input("Кубик владельца: "))
    if player >= owner:
        result = player - owner
        print(f"Разность: {result}")
        print("Игрок платит")
    else:
        result = player + owner
        print(f"Сумма: {result}")
        print("Владелец платит")
    print("Игра окончена")

# Задача 7. Хватит ли зарплаты
def salary_check():
    hours = int(input("Введите отработанные часы: "))
    credit = int(input("Введите остаток по кредиту: "))
    food = int(input("Введите траты на еду: "))
    salary = (hours * 500) - (hours * 50)
    if salary >= credit + food:
        print("Часов хватает. Можно отдохнуть")
    else:
        print("Часов не хватает. Придётся работать больше!")

# Задача 8. Максимальное число (по желанию)
def max_number():
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    num3 = int(input("Введите третье число: "))
    max_num = max(num1, num2, num3)
    print(f"Максимальное число: {max_num}")

# Вызов всех функций для выполнения задач
weather_sensor()
admission()
schedule()
discount_calculator()
absolute_value()
dice_game()
salary_check()
max_number()