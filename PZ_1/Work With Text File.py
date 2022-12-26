X = int(3)
while(X>0):
    name = str("Имя:"+input('Введите Имя: '))
    fname = str("Фамилия:"+input('Введите Фамилию: '))
    year = str("Возраст:"+input('Введите возраст: '))
    town = str('Город:'+input('Введите город: '))
    street = str("Улица:"+input('Введите улицу: '))
    house = str("Дом:"+input('Введите номер дома: '))
    I = [name, fname, year, town, street, house]
    f1 = open("Work.txt", "a", encoding='UTF-8')
    for item in I:
        f1.write("%s\xa0" % item)
    f1.write('\n')
    X -= 1
f1.close()
f1 = open("Work.txt")
k = f1.read()
print(k)
