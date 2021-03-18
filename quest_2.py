with open("my_read.txt", 'r', encoding="utf-8") as f:
    date = f.readlines()
    print(len(date))
    i = 1
    for el in date:
        el = el.split()
        if len(el)>5:
            print(f"{len(el)} слов")
        elif len(el) == 1:
            print(f"{len(el)} слово")
        else:
            print(f"{len(el)} слова")
        i += 1
