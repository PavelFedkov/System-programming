import re
import threading
import shutil



def writer(x, event_for_wait, event_for_set):
    for i in range(1):
        event_for_wait.wait() # wait for event
        event_for_wait.clear() # clean event for future
        print (x)
        event_for_set.set() # set event for neighbor thread

p=re.compile(r'\d.')
p1=re.compile(r'\w.')
f2=open("second.txt","w")
f3 =open("third.txt","w")
with open('first.txt','r',encoding='utf-8')as file:
     text = file.read()
     stage=re.findall(p,text)
     f2.write((f'Количество чисел: {len(stage)}\n'))
with open('first.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    stage = re.findall(p1, text)
    f3.write((f'Количество букв: {len(stage)}\n'))

with open('first.txt','r',encoding='utf-8') as first, open('final.txt', 'w') as second:
    data = first.read()
    second.write(data)
f4 = open("final.txt","a+")
f4.write('\n')
f2=open("second.txt","r")
f4.write(f2.read())
f3 =open("third.txt","r")
f4.write('\n')
f4.write(f3.read())
# init events
e1 = threading.Event()
e2 = threading.Event()
e3 = threading.Event()
e4 = threading.Event()
# init threads
t1 = threading.Thread(name = "")
t2 = threading.Thread(name = "Занесение кол-ва чисел во второй файл")
t3 = threading.Thread(name = "Занесение кол-ва букв в третий файл")
t4 = threading.Thread(name = "Создание и заполнение статистического файла")
t1 = threading.Thread(target=writer, args=("Открытие начального файла", e1 , e2))
t2 = threading.Thread(target=writer, args=("Подсчет количества чисел в файле", e2, e3))
t3 = threading.Thread(target=writer, args=("Подсчет количества чисел в файле", e3, e4))
t4 = threading.Thread(target=writer, args=("Создание финального файла", e4, e1))
# start threads
t1.start()
t2.start()
t3.start()
t4.start()
e1.set() # initiate the first event

# join threads to the main thread
t1.join()
t2.join()
t3.join()
t4.join()