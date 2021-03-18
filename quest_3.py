with open("text_3.txt", 'r', encoding='utf-8') as f:
    data = f.readlines()
    sum = 0;
    print("Меньше 20 тыс. получают: ")
    n = 0
    for el in data:
        el = el.split()
        try:
            el_sum = float(el[1])
            if el_sum <= 20000:
                print(f"{el[0]}")
            sum = sum + el_sum
            n += 1
        except ValueError:
            print("Зарплата задана неверно")
    print(f"Средняя зарплата всех сотрудников равна {sum / n}")
