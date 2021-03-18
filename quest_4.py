from translate import Translator

translator = Translator(from_lang="en", to_lang="ru")
with open('text_4.txt', 'r', encoding='utf-8') as f_1:
    f_2 = open('my_write.txt', 'w', encoding='utf-8')
    date = f_1.readlines()
    for el in date:
        el = el.split()
        el[0] = translator.translate(el[0])
        el = el[0] + ' ' + el[1] + ' ' + el[2]
        f_2.write(el + '\n')
    f_2.close()
