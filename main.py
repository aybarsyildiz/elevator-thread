import threading
import time
import random

asansor = []
toplam_musteri_sayisi = 0
suAnKat = 0

def get_input():
    input1 = input()
    asansor.append(input1)

def musteri_giris():
    toplam_musteri_sayisi += random.randint(1,10)

def musteri_cikis():
    toplam_musteri_sayisi -= random.randint(1,5)
    
def increment():
    global suAnKat
    suAnKat+=1
    time.sleep(2)
    print("Yukarıya doğru gidiyor, bulunduğu kat: ", suAnKat)
    
def decrement():
    global suAnKat
    suAnKat-=1
    time.sleep(2)
    print("Aşağıya doğru gidiyor, bulunduğu kat: ", suAnKat)
    
def traverse():
    if asansor:
        while(True):
            if asansor:
                if(suAnKat > int(asansor[0])):
                    decrement()
                    
                if(str(suAnKat) in asansor):
                    print("Asansör durdu, bulunduğu kat: ", suAnKat)
                    asansor.remove(str(suAnKat))
                    break
                    
                if(suAnKat < int(asansor[0])):
                    increment()
    

if __name__ == '__main__':
    print("Asansörün gitmesini istediğiniz kat numarasını giriniz: ", end="")
    while(True):
        t1= threading.Thread(target=get_input, name='t1')
        t2= threading.Thread(target=traverse, name='t2')
        t1.start()
        time.sleep(5)
        traverse()
        t2.start()