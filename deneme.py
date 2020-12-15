import threading
import time
import random
import tkinter as tk

kat =[0,0,0,0,0]#Kattaki kişiler

çıkışKat=[0,0,0,0]#Kattan çıkmak isteyen kişiler

asansor=[[True,True,0,0],[False,True,0,0],[False,True,0,0],[False,True,0,0],[False,True,0,0]] #[Çalışıyo mu, Yukarı çıkıyor mu, kaçıncı katta, kaç kişi var]


start = time.perf_counter()

def çalışıyormu(sayi):
    
    if asansor[sayi][0]==True:
        mesaj="Çalışıyor"
    else:
        mesaj="Çalışmıyor"
    return mesaj



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
    
    #print(katlar)
    return katlar


def exit():#Düzenle
    global çıkışKat
    global kat
    global asansor
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

def denetle():
    global kat
    global çıkışKat
    global asansor
    
    while True:
        toplamKuyruk=kat[0]+çıkışKat[0]+çıkışKat[1]+çıkışKat[2]+çıkışKat[3]
        asansorSayısı=0
        
        for i in range(5):
            if asansor[i][0]==True:
                asansorSayısı+=1
        
        asansorIhtiyacı=(toplamKuyruk//10)
        if asansorIhtiyacı>4:
            asansorIhtiyacı=4
        print("  ",asansorIhtiyacı)
        for i in range (1,5):
            if asansorIhtiyacı>0:
                asansor[i][0]=True
            else:
                if asansor[i][2]==0:
                    asansor[i][3]=0
                    asansor[i][0]=False

        
        time.sleep(0.2)


                

           




def asansor1(sayi):
    global kat
    global asansor
    global çıkışKat
    
    while(True):
        if asansor[sayi][0]==True: #Asansör çalışıyo mu?
            
            if asansor[sayi][2]==0: #Asansör 0. katta mı?
                
                if asansor[sayi][3]>0: #Asansörde müşteri var mı?
                    asansor[sayi][3]=0 #Varsa insinler
                
                #elif asansor[0][3]==0: #Asansörde müşteri yok mu?
                    
                if kat[0]>=10: #Katta 10'dan fazla müşteri mi var 
                    asansor[sayi][3]=10 #Varsa 10 kişi al
                    kat[0]-=10 #0.kattan 10 kişi eksilt
                    katlar = gidilecekKatlar(10)
                else: #Katta 10'dan az kişi varsa
                    asansor[sayi][3]=kat[0] #Kattaki herkesi al
                    kat[0]=0 #Katı boşalt
                    katlar = gidilecekKatlar(kat[0])
            
                asansor[sayi][2]+=1 #Yukarı çık
                print(f"{sayi+1}.Asansor {asansor[sayi][2]}. katta")

            else: #0.Katta değilse
            
                if asansor[sayi][1]==True:
                    kat[asansor[sayi][2]] += katlar[asansor[sayi][2]-1] # Kat listesindeki insaları katlara aktar
                    asansor[sayi][3]-=katlar[asansor[sayi][2]-1] #Asansörden inen kişileri çıkar
                    katlar[asansor[sayi][2]-1]=0 #Bulunan Kat listesini Temizle
                   
                    if asansor[sayi][2]==4:
                    
                        if çıkışKat[asansor[sayi][2]-1]>=10:
                            asansor[sayi][3]+=10
                            kat[asansor[sayi][2]]-=10
                            çıkışKat[asansor[sayi][2]-1]-=10
                        else:
                            asansor[sayi][3]=çıkışKat[asansor[sayi][2]-1] #Çıkacak kişileri asansore al
                            kat[asansor[sayi][2]]-=çıkışKat[asansor[sayi][2]-1]
                            çıkışKat[asansor[sayi][2]-1]=0
                
                        asansor[sayi][2]-=2    
                        asansor[sayi][1]=False
               
                    asansor[sayi][2]+=1
                    print(f"{sayi+1}.Asansor {asansor[sayi][2]}. katta")
                else:
                
                    if  asansor[sayi][3] == 10:
                        print("Asansör dolu")
                    else:
                        if (asansor[sayi][3]+çıkışKat[asansor[sayi][2]-1])>=10:
                            asansor[sayi][3]+=(10-asansor[sayi][3])
                            kat[asansor[sayi][2]]-=(10-asansor[sayi][3])  
                            çıkışKat[asansor[sayi][2]-1]-=(10-asansor[sayi][3])
                        else:
                            asansor[sayi][3]+=çıkışKat[asansor[sayi][2]-1]          
                            kat[asansor[sayi][2]]-=çıkışKat[asansor[sayi][2]-1]
                            çıkışKat[asansor[sayi][2]-1]=0

                    asansor[sayi][2]-=1
                    print(f"{sayi+1}.Asansor {asansor[sayi][2]}. katta")
                    if asansor[sayi][2]==0:
                        asansor[sayi][1]=True

                
                


        time.sleep(1)


root =tk.Tk()
canvas = tk.Canvas(root, height=600 ,width=1300)
canvas.pack()

frame = tk.Frame(root,bg='#192633')
frame.place(relwidth=1,relheight=1)
#Asansör 1
label11=tk.Label(frame,text=str(çalışıyormu(0)),fg='white',bg='#192633')
label11.place(relx=0.03,rely=0.18,relwidth=0.16,relheight=0.12)

label12=tk.Label(frame,text="Naber",fg='white',bg='#192633')
label12.place(relx=0.03,rely=0.31,relwidth=0.16,relheight=0.12)

label13=tk.Label(frame,text="Naber",fg='white',bg='#192633')
label13.place(relx=0.03,rely=0.44,relwidth=0.16,relheight=0.12)

label14=tk.Label(frame,text="Naber",fg='white',bg='#192633')
label14.place(relx=0.03,rely=0.57,relwidth=0.16,relheight=0.12)

label15=tk.Label(frame,text="Naber",fg='white',bg='#192633')
label15.place(relx=0.03,rely=0.70,relwidth=0.16,relheight=0.12)
#Asansör2
label21=tk.Label(frame,text=str(çalışıyormu(1)),fg='white',bg='#192633')
label21.place(relx=0.22,rely=0.18,relwidth=0.16,relheight=0.12)

label22=tk.Label(frame,text="Naber",fg='white',bg='#192633')
label22.place(relx=0.22,rely=0.31,relwidth=0.16,relheight=0.12)

label23=tk.Label(frame,text="Naber",fg='white',bg='#192633')
label23.place(relx=0.22,rely=0.44,relwidth=0.16,relheight=0.12)

label24=tk.Label(frame,text="Naber",fg='white',bg='#192633')
label24.place(relx=0.22,rely=0.57,relwidth=0.16,relheight=0.12)

label25=tk.Label(frame,text="Naber",fg='white',bg='#192633')
label25.place(relx=0.22,rely=0.70,relwidth=0.16,relheight=0.12)
#Asansör3
label31=tk.Label(frame,text=str(çalışıyormu(2)),fg='white',bg='#192633')
label31.place(relx=0.41,rely=0.18,relwidth=0.16,relheight=0.12)

label32=tk.Label(frame,text="Naber",fg='white',bg='#192633')
label32.place(relx=0.41,rely=0.31,relwidth=0.16,relheight=0.12)

label33=tk.Label(frame,text="Naber",fg='white',bg='#192633')
label33.place(relx=0.41,rely=0.44,relwidth=0.16,relheight=0.12)

label34=tk.Label(frame,text="Naber",fg='white',bg='#192633')
label34.place(relx=0.41,rely=0.57,relwidth=0.16,relheight=0.12)

label35=tk.Label(frame,text="Naber",fg='white',bg='#192633')
label35.place(relx=0.41,rely=0.70,relwidth=0.16,relheight=0.12)
#Asansör4
label41=tk.Label(frame,text=str(çalışıyormu(3)),fg='white',bg='#192633')
label41.place(relx=0.60,rely=0.18,relwidth=0.16,relheight=0.12)

label42=tk.Label(frame,text="Naber",fg='white',bg='#192633')
label42.place(relx=0.60,rely=0.31,relwidth=0.16,relheight=0.12)

label43=tk.Label(frame,text="Naber",fg='white',bg='#192633')
label43.place(relx=0.60,rely=0.44,relwidth=0.16,relheight=0.12)

label44=tk.Label(frame,text="Naber",fg='white',bg='#192633')
label44.place(relx=0.60,rely=0.57,relwidth=0.16,relheight=0.12)

label45=tk.Label(frame,text="Naber",fg='white',bg='#192633')
label45.place(relx=0.60,rely=0.70,relwidth=0.16,relheight=0.12)
#Asansör5
label51=tk.Label(frame,text=str(çalışıyormu(4)),fg='white',bg='#192633')
label51.place(relx=0.79,rely=0.18,relwidth=0.16,relheight=0.12)

label52=tk.Label(frame,text="Naber",fg='white',bg='#192633')
label52.place(relx=0.79,rely=0.31,relwidth=0.16,relheight=0.12)

label53=tk.Label(frame,text="Naber",fg='white',bg='#192633')
label53.place(relx=0.79,rely=0.44,relwidth=0.16,relheight=0.12)

label54=tk.Label(frame,text="Naber",fg='white',bg='#192633')
label54.place(relx=0.79,rely=0.57,relwidth=0.16,relheight=0.12)

label55=tk.Label(frame,text="Naber",fg='white',bg='#192633')
label55.place(relx=0.79,rely=0.70,relwidth=0.16,relheight=0.12)

root.mainloop()





t1=threading.Thread(target=login)
t2=threading.Thread(target=exit)
t3=threading.Thread(target=asansor1,args=[0])
t4=threading.Thread(target=asansor1,args=[1])
t5=threading.Thread(target=asansor1,args=[2])
t6=threading.Thread(target=asansor1,args=[3])
t7=threading.Thread(target=asansor1,args=[4])
t8=threading.Thread(target=denetle)
root.mainloop()
#t1=threading.Thread(target=login)
z=threading.Thread(target=root.mainloop)
z.start()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()


t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()





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