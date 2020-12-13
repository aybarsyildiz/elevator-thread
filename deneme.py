import threading
import time
import random

kat =[0,5]
"""
kat0=0
kat1=0
kat1K=0
kat2=0
kat2K=0
kat3=0
kat3K=0
kat4=0
kat4K=0
"""
asansor1=[True,0]
asansor2=[False,0]
asansor3=[False,0]
asansor4=[False,0]
asansor5=[False,0]

start = time.perf_counter()

def login():
    global kat
    while(True):
       giriş =random.randint(1,10)
       kat[0] +=giriş
       #print(kat[0])
       time.sleep(0.5)
      
      
           
 
def gidilecekKatlar(sayi):
    katlar=[0,0,0,0]
    for i in range(sayi):
        katlar[random.randint(0,3)]+=1
    print(katlar)

def çıkış():
    katlar=[0,0,0,0]
    for i in range(5):
        katlar[random.randint(0,3)]+=1
    print(katlar)

def asanor(kat):
    while(True):
        for i in range(4):




    
"""
def do_something(seconds):
    print(f"Sleeping {seconds} second...")
    time.sleep(seconds)
    print("Done Sleeping")
"""

t1=threading.Thread(target=login)
#t1=threading.Thread(target=login)
#t1=threading.Thread(target=login)
#t1=threading.Thread(target=login)
#t1=threading.Thread(target=login)

t1.start()
t1.join()








"""
threadt=[]
threads=[]

for _ in range(1):
    t=threading.Thread(target=do_something,args=[2])
    t1=threading.Thread(target=login)
    t.start()
    t1.start()
    threads.append(t)
    threadt.append(t1)

for thread in threads:
    thread.join()

for thread in threadt:
    thread.join()   

gidilecekKatlar(10)

"""





"""

t2=threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()
"""

finish= time.perf_counter()

print(f"Finished in {round(finish-start,2)} second(s)")