import threading
import time
def sum(a , b):
        sum1 = a+b
        with open('first.txt','w+',encoding='utf-8')as file:
            file.write(f'Сумма: {sum1}\n')
            print(f'Сумма: {sum1}\n')


def mul(a,  b):
    mul1 = a * b
    with open('second.txt', 'w+', encoding='utf-8') as file:
        file.write(f'Произведение: {mul1}\n')
        print(f'Произведение: {mul1}\n')

def sub(a, b):
        time.sleep(2)
        sub1 = a -b
        with open('third.txt', 'w+', encoding='utf-8') as file:
            file.write(f'Вычитание: {sub1}\n')
            print(f'Вычитание: {sub1}\n')

def div(a, b):
        time.sleep(1)
        div1 = a / b
        with open('final.txt', 'w+', encoding='utf-8') as file:
            file.write(f'Деление: {div1}\n')
            print(f'Деление: {div1}\n')
with open('fatality.txt', 'w+', encoding='windows-1251') as fil:
    f1 = open('first.txt','r')
    f2 = open('second.txt','r')
    f3 =open('third.txt','r')
    f4 =open('final.txt','r')
    print( f1.read(), '\n', f2.read(), '\n',
                      f3.read(),'\n', f4.read() , '\n', file=fil)

e1 = threading.Event()
e2 = threading.Event()
e3 = threading.Event()
e4 = threading.Event()

t1 = threading.Thread(target=sum, args=(3 , 5))
t2 = threading.Thread(target=mul, args=(10 , 25))
t3 = threading.Thread(target=sub, args=(11 , 9))
t4 = threading.Thread(target=div, args=(20 , 4))

t1.start()
t2.start()
t3.start()
t4.start()

e1.set()

t1.join()
t2.join()
t3.join()
t4.join()