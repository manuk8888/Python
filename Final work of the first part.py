# Задача: MyProfile для предпринимателей
def myprofile():
    # Инициализация переменных
    personal_info = {
        "Имя": "",
        "Возраст": 0,
        "Телефон": "",
        "Электронная почта": "",
        "Индекс": "",
        "Почтовый адрес": "",
        "Дополнительная информация": ""
    }
    business_info = {
        "ОГРНИП": "",
        "ИНН": "",
        "Расчётный счёт": "",
        "Название банка": "",
        "БИК": "",
        "Корреспондентский счёт": ""
    }

    # Функция для ввода личной информации
    def input_personal_info():
        personal_info["Имя"] = input("Введите имя: ")
        while True:
            try:
                age = int(input("Введите возраст: "))
                if age >= 0:
                    personal_info["Возраст"] = age
                    break
                else:
                    print("Возраст должен быть неотрицательным числом.")
            except ValueError:
                print("Возраст должен быть целым числом.")
        personal_info["Телефон"] = input("Введите телефон: ")
        personal_info["Электронная почта"] = input("Введите электронную почту: ")
        index = input("Введите индекс: ")
        personal_info["Индекс"] = ''.join(filter(str.isdigit, index))  # Оставляем только цифры
        personal_info["Почтовый адрес"] = input("Введите почтовый адрес: ")
        personal_info["Дополнительная информация"] = input("Введите дополнительную информацию: ")

    # Функция для ввода информации о предпринимателе
    def input_business_info():
        while True:
            ogrnip = input("Введите ОГРНИП (15 цифр): ")
            if ogrnip.isdigit() and len(ogrnip) == 15:
                business_info["ОГРНИП"] = ogrnip
                break
            else:
                print("ОГРНИП должен содержать ровно 15 цифр.")
        while True:
            inn = input("Введите ИНН: ")
            if inn.isdigit():
                business_info["ИНН"] = inn
                break
            else:
                print("ИНН должен содержать только цифры.")
        while True:
            account = input("Введите расчётный счёт (20 цифр): ")
            if account.isdigit() and len(account) == 20:
                business_info["Расчётный счёт"] = account
                break
            else:
                print("Расчётный счёт должен содержать ровно 20 цифр.")
        business_info["Название банка"] = input("Введите название банка: ")
        while True:
            bik = input("Введите БИК: ")
            if bik.isdigit():
                business_info["БИК"] = bik
                break
            else:
                print("БИК должен содержать только цифры.")
        while True:
            corr_account = input("Введите корреспондентский счёт: ")
            if corr_account.isdigit():
                business_info["Корреспондентский счёт"] = corr_account
                break
            else:
                print("Корреспондентский счёт должен содержать только цифры.")

    # Функция для вывода личной информации
    def print_personal_info():
        print("\nЛичная информация:")
        for key, value in personal_info.items():
            print(f"{key}: {value}")

    # Функция для вывода всей информации
    def print_full_info():
        print("\nВся информация:")
        for key, value in personal_info.items():
            print(f"{key}: {value}")
        for key, value in business_info.items():
            print(f"{key}: {value}")

    # Главное меню
    while True:
        print("\nГлавное меню:")
        print("1 — Ввести или обновить информацию")
        print("2 — Вывести информацию")
        print("0 — Завершить работу")
        choice = input("Введите номер пункта меню: ")

        if choice == "1":
            while True:
                print("\nПодменю ввода информации:")
                print("1 — Личная информация")
                print("2 — Информация о предпринимателе")
                print("0 — Назад")
                sub_choice = input("Введите номер пункта меню: ")

                if sub_choice == "1":
                    input_personal_info()
                elif sub_choice == "2":
                    input_business_info()
                elif sub_choice == "0":
                    break
                else:
                    print("Введён некорректный пункт меню.")
        elif choice == "2":
            while True:
                print("\nПодменю вывода информации:")
                print("1 — Личная информация")
                print("2 — Вся информация")
                print("0 — Назад")
                sub_choice = input("Введите номер пункта меню: ")

                if sub_choice == "1":
                    print_personal_info()
                elif sub_choice == "2":
                    print_full_info()
                elif sub_choice == "0":
                    break
                else:
                    print("Введён некорректный пункт меню.")
        elif choice == "0":
            print("Завершение работы.")
            break
        else:
            print("Введён некорректный пункт меню.")

# Запуск программы
myprofile()