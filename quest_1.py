f = open('my_read.txt', 'w', encoding='utf-8')
while True:
    date = input("Введите строку. Для отмены введите пробел: ")
    a = []
    if date.split() == a:
        print("Прекращение выполнения программы.")
        break
    else:
        f.write(date + '\n')
f.close()


