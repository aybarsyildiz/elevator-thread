import threading
import time
import random
import PySimpleGUI as sg

asansor = []
toplam_musteri_sayisi = 0
musteri_queue = [[5,3],[3,4],[1,1],[2,3],[6,5],[3,2]] #müşteri sayısı - gideceği kat


#layout = [[sg.Text("Müşteriler")],[sg.Text(str(musteri_queue))]]
suAnKat = 0
#window = sg.Window("elevator thread",layout, margins=(400,350))

def get_input():
    input1 = input()
    asansor.append(input1)

def musteri_giris():
    #toplam_musteri_sayisi += random.randint(1,10)
    musteri_queue.append([random.randint(1,10),random.randint(1,5)])
    asansor.append(musteri_queue[0][1])
    
    
def musteri_cikis():
    #toplam_musteri_sayisi -= random.randint(1,5)
    return musteri_queue.pop(0)
    
def increment():
    global suAnKat
    suAnKat+=1
    time.sleep(0.2)
    print("Yukarıya doğru gidiyor, bulunduğu kat: ", suAnKat)
    
def decrement():
    global suAnKat
    suAnKat-=1
    time.sleep(0.2)
    print("Aşağıya doğru gidiyor, bulunduğu kat: ", suAnKat)
    
def traverse(i):
    if asansor:
        print(i,". asansörün gideceği kat: ",asansor[0])
        while(True):
            
            if asansor:
                2
                if(suAnKat > asansor[0]):
                    decrement()
                    
                if(suAnKat == asansor[0]):
                    print("Asansör durdu, bulunduğu kat: ", suAnKat)
                    asansor.pop(0)
                    musteri_cikis()
                    
                    asansor.append(musteri_queue[0][1])
                    break
                    
                if(suAnKat < asansor[0]):
                    increment()
    

if __name__ == '__main__':
    
    print(musteri_queue)
    
    while(True):
        musteri_giris()
        #event, values = window.read()
        gidilecek_kat = musteri_queue[0][1]
        print("QUEUE BOYUT:",len(musteri_queue) )
        print("Zemin kattaki müşteriler: ",musteri_queue)
        
        t1= threading.Thread(target=musteri_giris, name='t1')
        if(len(musteri_queue)>0):
            t2= threading.Thread(target=traverse(1), name='t2')
        musteri_giris()
        if(len(musteri_queue)>6):
            t3=threading.Thread(target=traverse(2), name='t3')
        musteri_giris()
        if(len(musteri_queue)>12):
            t4 = threading.Thread(target=traverse(3), name='t4')
        if(len(musteri_queue)>18):
            t5 = threading.Thread(target=traverse(4),name='t5')
        if(len(musteri_queue)>24):
            t6 = threading.Thread(target=traverse(5), name='t6')
        
        
       
        
        
    """
        if(len(musteri_queue)>0):
            print("KONTROL1")
            t2.start()
            
            
        if(len(musteri_queue)>6):   
            print("KONTROL2 ")  
            t3.start()
            
            
        if(len(musteri_queue)>12):
            t4.start()
        
        if(len(musteri_queue)>18):
            t5.start()
            
        if(len(musteri_queue)>24):
            t6.start()
    """        
    time.sleep(0.5)

        
    