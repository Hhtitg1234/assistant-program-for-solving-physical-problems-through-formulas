print("""
by Hhtitg_1234_
version 1.00\n""")

# Главное меню
a = False
while a == False:
    print("Перед вами список процессов, которые можно узнать:\n")
    print("кпд\nсгорание топлива\nплавление\nпарообразование\nсвт\nсправка\nвыход\n")

    p = input("Введите показатель, который нужно расчитать, с маленькой буквы, так, как написано в списке: ")
    if p == 'кпд':
        q = False
        while q == False:
            b = input("Что нужно узнать: кпд, а полезное, а затраченное, выход: ")
            if b == 'кпд':
                A_pol = int(input("Введите А полезное, без единиц измерения: "))
                A_zatr = int(input("Введите А затраченное, без единиц измерения: "))
                kpd = A_pol / A_zatr * 100
                print()
                print("Ответ:", kpd, "%\n")
                q = True
            elif b == 'а полезное':
                kpd = int(input("Введите кпд, без процентов: "))
                A_zatr = int(input("Введите А затраченное, без единиц измерения: "))
                A_pol = kpd / 100 * A_zatr
                print()
                print("Ответ:", A_pol, "Дж\n")
                q = True
            elif b == 'а затраченное':
                kpd = int(input("Введите кпд, без процентов: "))
                A_pol = int(input("Введите а полезное, без единиц измерения: "))
                A_zatr = A_pol / (kpd / 100)
                print()
                print("Ответ:", A_zatr, "Дж\n")
                q = True
            elif b == 'выход':
                print()
                q = True
            else:
                print("Введены некорректные данные или написана неправильная буква>>>")

    elif p == 'плавление':
        r = False
        while r == False:
            o = input("Введите что нужно узнать: удельная теплота плавления, масса, выход: ")
            if o == 'удельная теплота плавления':
                mas = int(input("Введите массу в кг без единиц измерения: "))
                print()
                print(
                    "Аллюминий = 390.000 Дж/кг\nЖелезо = 270.000 Дж/кг\nЗолото = 67.000 Дж/кг\nЛед = 340.000 Дж/кг\nМедь = 210.000 Дж/кг\nНафталин = 150.000 Дж/кг\nОлово = 59.000 Дж/кг")
                print(
                    "Платина = 110.000 Дж/кг\nРтуть = 10.000 Дж/кг\nСвинец = 25.000 Дж/кг\nСеребро = 100.000 Дж/кг\nЦинк = 120.000 Дж/кг\nЧугун белый = 140.000 Дж/кг\nЧугун серый = 100.000 Дж/кг\n")
                lam = int(input("Введите удельную теплоту плавления (лямбда) вещества в Дж/кг без единиц измерений: "))
                qu_ob = lam * mas
                print("Ответ:", qu_ob, "Дж\n")
                r = True
            elif o == 'масса':
                qu_ob = int(input("Введите удельную теплоту плавления (Q) вещества в Дж без единиц измерений: "))
                print()
                print(
                    "Аллюминий = 390.000 Дж/кг\nЖелезо = 270.000 Дж/кг\nЗолото = 67.000 Дж/кг\nЛед = 340.000 Дж/кг\nМедь = 210.000 Дж/кг\nНафталин = 150.000 Дж/кг\nОлово = 59.000 Дж/кг")
                print(
                    "Платина = 110.000 Дж/кг\nРтуть = 10.000 Дж/кг\nСвинец = 25.000 Дж/кг\nСеребро = 100.000 Дж/кг\nЦинк = 120.000 Дж/кг\nЧугун белый = 140.000 Дж/кг\nЧугун серый = 100.000 Дж/кг\n")
                lam = int(input("Введите удельную теплоту плавления (лямбда) вещества в Дж/кг без единиц измерений: "))
                mas = qu_ob / lam
                print("Ответ:", mas, "кг\n")
                r = True
            elif o == 'выход':
                print()
                r = True
            else:
                print("Введены некорректные данные или написана неправильная буква>>>")

    elif p == 'сгорание топлива' or p == 'сгорание':
        w = False
        while w == False:
            c = input("Введите что нужно узнать: удельная теплота сгорания, масса, выход: ")
            if c == 'удельная теплота сгорания':
                massa = int(input("Введите массу в кг без единиц измерения: "))
                print()
                print(
                    "Бензин = 46.000.000 Дж/кг\nБурый уголь = 17.000.000 Дж/кг\nВодород = 120.000.000 Дж/кг\nДизельное топливо = 42.700.000 Дж/кг")
                print(
                    "Сухие дрова = 13.000.000 Дж/кг\nДревесный уголь = 34.000.000 Дж/кг\nКаменный уголь = 30.000.000 Дж/кг\nКеросин = 46.000.000 Дж/кг")
                print(
                    "Нефть = 44.000.000 Дж/кг\nПорох = 3.800.000 Дж/кг\nПриродный газ = 44.000.000 Дж/кг\nСпирт = 27.000.000 Дж/кг\nТорф = 14.000.000 Дж/кг")
                print()
                q_ob = int(input("Введите удельную теплоту сгорания вещества в Дж без единиц измерения: "))
                ud_t = q_ob * massa
                print()
                print("Ответ:", ud_t, "Дж\n")
                w = True
            elif c == 'масса':
                ud_t = int(input("Введите удельную теплоту сгорания в Дж без единиц измерения: "))
                print()
                print(
                    "Бензин = 46.000.000 Дж/кг\nБурый уголь = 17.000.000 Дж/кг\nВодород = 120.000.000 Дж/кг\nДизельное топливо = 42.700.000 Дж/кг")
                print(
                    "Сухие дрова = 13.000.000 Дж/кг\nДревесный уголь = 34.000.000 Дж/кг\nКаменный уголь = 30.000.000 Дж/кг\nКеросин = 46.000.000 Дж/кг")
                print(
                    "Нефть = 44.000.000 Дж/кг\nПорох = 3.800.000 Дж/кг\nПриродный газ = 44.000.000 Дж/кг\nСпирт = 27.000.000 Дж/кг\nТорф = 14.000.000 Дж/кг")
                print()
                q_ob = int(input("Введите удельную теплоту сгорания вещества в Дж без единиц измерения: "))
                massa = ud_t / q_ob
                print()
                print("Ответ:", massa, "кг\n")
                w = True
            elif c == 'выход':
                print()
                w = True
            else:
                print("Введены некорректные данные или написана неправильная буква>>>")

    elif p == 'справка':
        print()
        print("Перед вами справка по эксплуатации программы-помощника по решению физических задач через формулы")
        print("1) обязательно вводите все названия с маленькой буквы, так, как они написаны в предложенном списке")
        print("Пример: Введите что нужно узнать: кпд")
        print(
            "2) если не хотите вписывать названия вручную, можно их копировать(зависит от программы, которую вы используете)")
        print(
            "3) в местах, где есть списки с цифрами, есть запятые, при записи цифр не нужно писать запятые и единицы измерения")
        print(
            "4) по всем неполадкам или предложениям с добавлением новых функций можно писать сюда: maximpetrov2806@gmail.com")
        print()

    elif p == 'свт':
        i = False
        while i == False:
            vopr = input("Введите что нужно узнать: (расстояние, скорость, время, выход)\n")
            b = 0
            if vopr == 'расстояние':
                v = int(input("Введите скорость в м.с: "))
                t = int(input("Введите время в секундах: "))
                b = v * t
                print()
                print("Ответ:", b, 'метр-(ов)')
                i = True
            elif vopr == 'скорость':
                s = int(input("Введите расстояние в метрах: "))
                t = int(input("Введите время в секундах: "))
                b = s / t
                print()
                print("Ответ:", b, "м/с\n")
                i = True
            elif vopr == 'время':
                s = int(input("Введите расстояние в метрах: "))
                v = int(input("Введите скорость в м.с: "))
                b = s / v
                print()
                print("Ответ:", b, "секунд\n")
                i = True
            elif vopr == 'выход':
                print()
                i = True
                break
            else:
                print("Введены некорректные данные или написана неправильная буква>>>")

    elif p == 'парообразование':
        e = False
        while e == False:
            d = input("Введите что нужно узнать: удельная теплота парообразования, масса, выход: ")
            if d == 'удельная теплота парообразования':
                print()
                print("Вода = 2.300.000 Дж/кг\nРтуть = 300.000 Дж/кг\nСпирт = 900.000 Дж/кг\nЭфир = 400.000 Дж/кг\n")
                l = int(input("Введите удельную теплоту парообразования вещества в Дж без единиц измерения: "))
                mass = int(input("Введите массу вещества в кг без единиц измерения: "))
                x = l * mass
                print()
                print("Ответ:", x, "Дж\n")
                e = True
            elif d == 'масса':
                print()
                print("Вода = 2.300.000 Дж/кг\nРтуть = 300.000 Дж/кг\nСпирт = 900.000 Дж/кг\nЭфир = 400.000 Дж/кг\n")
                l = int(input("Введите удельную теплоту парообразования вещества в Дж без единиц измерения: "))
                t_p = int(input("Введите удельную теплоту парообразования в Дж без единиц измерения: "))
                mass = t_p / l
                print()
                print("Ответ:", mass, "кг\n")
                e = True
            elif d == 'выход':
                print()
                e = True
            else:
                print("Введены некорректные данные или написана неправильная буква>>>")

    elif p == 'выход':
        a = True
        break