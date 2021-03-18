with open('my_write_5.txt', 'w', encoding='utf-8') as f_1:
    num = input("Введите числа: ")
    for i in num.split():
        try:
            i = float(i)
            f_1.write(str(i) + ' ')
        except ValueError:
            print("Введено не число")
with open('my_write_5.txt', 'r', encoding='utf-8') as f_2:
    date = f_2.read().split()
    sum = 0
    for i in date:
        i = float(i)
        sum += i
print(sum)
