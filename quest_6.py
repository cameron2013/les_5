with open('text_6.txt', 'r', encoding='utf-8') as f:
    date = f.readlines()
    x = {}
    for el in date:
        el = el.split()
        el[0] = el[0][:len(el[0]) - 1]
        a = 0
        i = 1
        while i <= len(el) - 1:
            if el[i] != '-':
                a = a + int(el[i][:el[i].index('(')])
            i += 1
        x[el[0]] = a
print(x)
