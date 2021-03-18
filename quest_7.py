import json

with open('text_7.txt', 'r', encoding='utf-8') as f_1:
    data = f_1.readlines()
    x = {}
    y = {}
    sum_av = 0
    n = 0
    for el in data:
        el = el.split()
        try:
            result = float(el[2]) - float(el[3])
            if result >= 0:
                sum_av = sum_av + result
                n += 1
        except ValueError:
            print("Неверные данные")
        x[el[0]] = result
y["average_profit"] = sum_av / n
with open('text_7.json', 'w', encoding='utf-8') as f_2:
    json.dump([x, y], f_2)
