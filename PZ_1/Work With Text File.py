selects = int(input('Если хотите записать в столбик то введите 1, если в строчку то 2:\n '))
name = str("Имя:"+input('Введите Имя: '))
fname = str("Фамилия:"+input('Введите Фамилию: '))
year = str("Возраст:"+input('Введите возраст: '))
town = str('Город:'+input('Введите город: '))
street = str("Улица:"+input('Введите улицу: '))
house = str("Дом:"+input('Введите номер дома: '))
I = [name, fname, year, town, street, house]
f1 = open("Work.txt", "a")
if selects == 1:
    f1.write('\n')
    for item in I:
        f1.write("%s\n" % item)
    f1.write('\n')
else:
    for item in I:
        f1.write("%s\xa0" % item)
    f1.write('\n')
f1.close()
f1 = open("Work.txt")
k = f1.read()
print(k)
