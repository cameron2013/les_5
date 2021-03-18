with open("my_read.txt", 'r', encoding="utf-8") as f:
    date = f.readlines()
    print(len(date))
    i = 1
    for el in date:
        el = el.split()
        if i == 2:
            if len(el) < 5:
                print(f"Во {i}-ой строке {len(el)} слова")
            else:
                print(f"Во {i}-ой строке {len(el)} слов")
        else:
            if len(el) < 5:
                print(f"Во {i}-ой строке {len(el)} слова")
            else:
                print(f"Во {i}-ой строке {len(el)} слов")
        i += 1
