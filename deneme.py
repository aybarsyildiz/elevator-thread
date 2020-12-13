import threading
import time
import random

kat =[0,0,0,0,0]#Kattaki kişiler

çıkışKat=[0,0,0,0]#Kattan çıkmak isteyen kişiler

asansor=[[True,0,0],[False,0,0],[False,0,0],[False,0,0],[False,0,0]] #[Çalışıyo mu, kaçıncı katta, kaç kişi var]


start = time.perf_counter()

def login():
    global kat
    while(True):
       giriş =random.randint(1,10)
       kat[0] +=giriş
       print(kat[0])
       time.sleep(0.5)
      
      
def gidilecekKatlar(sayi):
    katlar=[0,0,0,0]
    for i in range(sayi):
        katlar[random.randint(0,3)]+=1
    
    print(katlar)
    return katlar


def exit():
    global çıkışKat
    global kat
    while(True):
        for i in range(5):
            x=random.randint(1,4)
            if kat[x]==0:
                while kat[x]>0:
                    x=random.randint(1,4)
            else:
                çıkışKat[x-1]+=1
                kat[x]-=1

    time.sleep(1)

"""
def asanor1():
    global kat
    global asansor
    while(True):
        asansorler=0
        for i in range(4):
            if asansor[i][0]==True:
                asansorler+=1
        
        if kat[0]>10:
            katlar=gidilecekKatlar(10)
        elif kat[0]<0:
            katlar=gidilecekKatlar(kat[0])
    
    time.sleep(0.2)

def asanor2():
    global kat
    global asansor
    while(True):
        asansorler=0
        for i in range(4):
            if asansor[i][0]==True:
                asansorler+=1
        
        if kat[0]>10:
            katlar=gidilecekKatlar(10)
        elif kat[0]<0:
            katlar=gidilecekKatlar(kat[0])
    
    time.sleep(0.2)

def asanor3():
    global kat
    global asansor
    while(True):
        asansorler=0
        for i in range(4):
            if asansor[i][0]==True:
                asansorler+=1
        
        if kat[0]>10:
            katlar=gidilecekKatlar(10)
        elif kat[0]<0:
            katlar=gidilecekKatlar(kat[0])
    
    time.sleep(0.2)

def asanor4():
    global kat
    global asansor
    while(True):
        asansorler=0
        for i in range(4):
            if asansor[i][0]==True:
                asansorler+=1
        
        if kat[0]>10:
            katlar=gidilecekKatlar(10)
        elif kat[0]<0:
            katlar=gidilecekKatlar(kat[0])
    
    time.sleep(0.2)

def asanor5():
    global kat
    global asansor
    while(True):
        asansorler=0
        for i in range(4):
            if asansor[i][0]==True:
                asansorler+=1
        
        if kat[0]>10:
            katlar=gidilecekKatlar(10)
        elif kat[0]<0:
            katlar=gidilecekKatlar(kat[0])
    
    time.sleep(0.2)
    
    
    def do_something(seconds):
    print(f"Sleeping {seconds} second...")
    time.sleep(seconds)
    print("Done Sleeping")

"""


t1=threading.Thread(target=login)
t2=threading.Thread(target=exit)
#t1=threading.Thread(target=login)
#t1=threading.Thread(target=login)
#t1=threading.Thread(target=login)

t1.start()
t2.start()

t1.join()
t2.join()








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

finish= time.perf_counter()

print(f"Finished in {round(finish-start,2)} second(s)")