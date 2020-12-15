import threading
import time
import random
import tkinter as tk


root =tk.Tk()
canvas = tk.Canvas(root, height=600 ,width=1300)
canvas.pack()

frame = tk.Frame(root,bg='#192633')
frame.place(relwidth=1,relheight=1)

label11=tk.Label(frame,text="Çalışıyor",fg='white',bg='#192633')
label11.place(relx=0.03,rely=0.18,relwidth=0.16,relheight=0.12)


label12=tk.Label(frame,text="",fg='white',bg='#192633')
label12.place(relx=0.03,rely=0.31,relwidth=0.16,relheight=0.12)

label13=tk.Label(frame,text="",fg='white',bg='#192633')
label13.place(relx=0.03,rely=0.44,relwidth=0.16,relheight=0.12)

label14=tk.Label(frame,text="",fg='white',bg='#192633')
label14.place(relx=0.03,rely=0.57,relwidth=0.16,relheight=0.12)

label15=tk.Label(frame,text="",fg='white',bg='#5E6770')
label15.place(relx=0.03,rely=0.70,relwidth=0.16,relheight=0.12)
    #Asansör2
    
label21=tk.Label(frame,text="",fg='white',bg='#192633')
label21.place(relx=0.22,rely=0.18,relwidth=0.16,relheight=0.12)
    

label22=tk.Label(frame,text="",fg='white',bg='#192633')
label22.place(relx=0.22,rely=0.31,relwidth=0.16,relheight=0.12)

label23=tk.Label(frame,text="",fg='white',bg='#192633')
label23.place(relx=0.22,rely=0.44,relwidth=0.16,relheight=0.12)

label24=tk.Label(frame,text="",fg='white',bg='#192633')
label24.place(relx=0.22,rely=0.57,relwidth=0.16,relheight=0.12)

label25=tk.Label(frame,text="",fg='white',bg='#5E6770')
label25.place(relx=0.22,rely=0.70,relwidth=0.16,relheight=0.12)
    #Asansör3
label31=tk.Label(frame,text="",fg='white',bg='#192633')
label31.place(relx=0.41,rely=0.18,relwidth=0.16,relheight=0.12)

label32=tk.Label(frame,text="",fg='white',bg='#192633')
label32.place(relx=0.41,rely=0.31,relwidth=0.16,relheight=0.12)

label33=tk.Label(frame,text="",fg='white',bg='#192633')
label33.place(relx=0.41,rely=0.44,relwidth=0.16,relheight=0.12)

label34=tk.Label(frame,text="",fg='white',bg='#192633')
label34.place(relx=0.41,rely=0.57,relwidth=0.16,relheight=0.12)

label35=tk.Label(frame,text="",fg='white',bg='#5E6770')
label35.place(relx=0.41,rely=0.70,relwidth=0.16,relheight=0.12)
    #Asansör4
label41=tk.Label(frame,text="",fg='white',bg='#192633')
label41.place(relx=0.60,rely=0.18,relwidth=0.16,relheight=0.12)

label42=tk.Label(frame,text="",fg='white',bg='#192633')
label42.place(relx=0.60,rely=0.31,relwidth=0.16,relheight=0.12)

label43=tk.Label(frame,text="",fg='white',bg='#192633')
label43.place(relx=0.60,rely=0.44,relwidth=0.16,relheight=0.12)

label44=tk.Label(frame,text="",fg='white',bg='#192633')
label44.place(relx=0.60,rely=0.57,relwidth=0.16,relheight=0.12)

label45=tk.Label(frame,text="",fg='white',bg='#5E6770')
label45.place(relx=0.60,rely=0.70,relwidth=0.16,relheight=0.12)
    #Asansör5
label51=tk.Label(frame,text="",fg='white',bg='#192633')
label51.place(relx=0.79,rely=0.18,relwidth=0.16,relheight=0.12)

label52=tk.Label(frame,text="",fg='white',bg='#192633')
label52.place(relx=0.79,rely=0.31,relwidth=0.16,relheight=0.12)

label53=tk.Label(frame,text="",fg='white',bg='#192633')
label53.place(relx=0.79,rely=0.44,relwidth=0.16,relheight=0.12)

label54=tk.Label(frame,text="",fg='white',bg='#192633')
label54.place(relx=0.79,rely=0.57,relwidth=0.16,relheight=0.12)

label55=tk.Label(frame,text="",fg='white',bg='#5E6770')
label55.place(relx=0.79,rely=0.70,relwidth=0.16,relheight=0.12)



kat =[0,0,0,0,0]#Kattaki kişiler
çıkışKat=[0,0,0,0]#Kattan çıkmak isteyen kişiler
asansor=[[True,True,0,0],[False,True,0,0],[False,True,0,0],[False,True,0,0],[False,True,0,0]] #[Çalışıyo mu, Yukarı çıkıyor mu, kaçıncı katta, kaç kişi var]


def çalışıyormu(sayi):
    
    if asansor[sayi][0]==True:
        mesaj="Çalışıyor"
        queue.put(mesaj)
    else:
        mesaj="Çalışmıyor"
        queue.put(mesaj)
    return mesaj


def yukarımı(sayi):  
    if asansor[sayi][1]==True:
        mesaj="Asansör yukarı çıkıyor"
    else:
        mesaj="Asansör aşşağı iniyor"
    return mesaj


def kaçkişi(sayi):
    mesaj="Asansörde",asansor[sayi][3],"kişi var"
    return mesaj

def kattakiKişiler(sayi):
    mesaj=sayi,".katta",kat[sayi],"kişi var"
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
    
    return katlar


def exit():
    global çıkışKat
    global kat
    global asansor
    while(True):
        for i in range(5):
            x=random.randint(1,4)
            if kat[x]<=0:
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
                asansorIhtiyacı-=1
                
                if i==1:
                    label21.configure(text="Çalışıyor")
                if i==2:
                    label31.configure(text="Çalışıyor")
                if i==3:
                    label41.configure(text="Çalışıyor")
                if i==4:
                    label51.configure(text="Çalışıyor")
                
                

                
            else:
                if asansor[i][2]==0:
                    asansor[i][3]=0
                    asansor[i][0]=False
                    if i==1:
                        label21.configure(text="Çalışmıyor")
                    if i==2:
                        label31.configure(text="Çalışmıyor")
                    if i==3:
                        label41.configure(text="Çalışmıyor")
                    if i==4:
                        label51.configure(text="Çalışmıyor")

        
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
                if sayi==0:
                    label12.configure(text=str(asansor[sayi][2]))
                    label13.configure(text=yukarımı(sayi))
                    label14.configure(text=kaçkişi(sayi))
                if sayi==1:
                    label22.configure(text=str(asansor[sayi][2]))
                    label23.configure(text=yukarımı(sayi))
                    label24.configure(text=kaçkişi(sayi))
                if sayi==2:
                    label32.configure(text=str(asansor[sayi][2]))
                    label33.configure(text=yukarımı(sayi))
                    label34.configure(text=kaçkişi(sayi))
                if sayi==3:
                    label42.configure(text=str(asansor[sayi][2]))
                    label43.configure(text=yukarımı(sayi))
                    label44.configure(text=kaçkişi(sayi))
                if sayi==4:
                    label52.configure(text=str(asansor[sayi][2]))
                    label53.configure(text=yukarımı(sayi))
                    label54.configure(text=kaçkişi(sayi))
                label15.configure(text=kattakiKişiler(0))
                label25.configure(text=kattakiKişiler(1))
                label35.configure(text=kattakiKişiler(2))
                label45.configure(text=kattakiKişiler(3))
                label55.configure(text=kattakiKişiler(4))
                
                


            else: #0.Katta değilse
            
                if asansor[sayi][1]==True:
                    kat[asansor[sayi][2]] += katlar[asansor[sayi][2]-1] # Kat listesindeki insaları katlara aktar
                    asansor[sayi][3]-=katlar[asansor[sayi][2]-1] #Asansörden inen kişileri çıkar
                    katlar[asansor[sayi][2]-1]=0 #Bulunan Kat listesini Temizle
                   
                    if asansor[sayi][2]==4: #Asansör 4. kattaysa
                    
                        if çıkışKat[asansor[sayi][2]-1]>=10: #çıkılacak katta 10 dan fazla kişi varsa
                            asansor[sayi][3]+=10
                            kat[asansor[sayi][2]]-=10
                            çıkışKat[asansor[sayi][2]-1]-=10
                        else:
                            asansor[sayi][3]=çıkışKat[asansor[sayi][2]-1] #Çıkacak kişileri asansore al
                            kat[asansor[sayi][2]]-=çıkışKat[asansor[sayi][2]-1] #Kattan çıkan kadar eksilt
                            çıkışKat[asansor[sayi][2]-1]=0 #çıkış listesinden çıkan kadar çıkart
                
                        asansor[sayi][2]-=2    
                        asansor[sayi][1]=False
               
                    asansor[sayi][2]+=1
                    print(f"{sayi+1}.Asansor {asansor[sayi][2]}. katta")
                    if sayi==0:
                        label12.configure(text=str(asansor[sayi][2]))
                        label13.configure(text=yukarımı(sayi))
                        label14.configure(text=kaçkişi(sayi))
                    if sayi==1:
                        label22.configure(text=str(asansor[sayi][2]))
                        label23.configure(text=yukarımı(sayi))
                        label24.configure(text=kaçkişi(sayi))
                    if sayi==2:
                        label32.configure(text=str(asansor[sayi][2]))
                        label33.configure(text=yukarımı(sayi))
                        label34.configure(text=kaçkişi(sayi))
                    if sayi==3:
                        label42.configure(text=str(asansor[sayi][2]))
                        label43.configure(text=yukarımı(sayi))
                        label44.configure(text=kaçkişi(sayi))
                    if sayi==4:
                        label52.configure(text=str(asansor[sayi][2]))
                        label53.configure(text=yukarımı(sayi))
                        label54.configure(text=kaçkişi(sayi))
                    label15.configure(text=kattakiKişiler(0))
                    label25.configure(text=kattakiKişiler(1))
                    label35.configure(text=kattakiKişiler(2))
                    label45.configure(text=kattakiKişiler(3))
                    label55.configure(text=kattakiKişiler(4))
               
               
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
                    if sayi==0:
                        label12.configure(text=str(asansor[sayi][2]))
                        label13.configure(text=yukarımı(sayi))
                        label14.configure(text=kaçkişi(sayi))
                    if sayi==1:
                        label22.configure(text=str(asansor[sayi][2]))
                        label23.configure(text=yukarımı(sayi))
                        label24.configure(text=kaçkişi(sayi))
                         
                    if sayi==2:
                        label32.configure(text=str(asansor[sayi][2]))
                        label33.configure(text=yukarımı(sayi))
                        label34.configure(text=kaçkişi(sayi))
                         
                    if sayi==3:
                        label42.configure(text=str(asansor[sayi][2]))
                        label43.configure(text=yukarımı(sayi))
                        label44.configure(text=kaçkişi(sayi))
                    if sayi==4:
                        label52.configure(text=str(asansor[sayi][2]))
                        label53.configure(text=yukarımı(sayi))
                        label54.configure(text=kaçkişi(sayi))
                    label15.configure(text=kattakiKişiler(0))
                    label25.configure(text=kattakiKişiler(1))
                    label35.configure(text=kattakiKişiler(2))
                    label45.configure(text=kattakiKişiler(3))
                    label55.configure(text=kattakiKişiler(4))
                    
                    if asansor[sayi][2]==0:
                        asansor[sayi][1]=True

                
                


        time.sleep(1)


    
    

    
    

      


    



t1=threading.Thread(target=login)
t2=threading.Thread(target=exit)
t3=threading.Thread(target=asansor1,args=[0])
t4=threading.Thread(target=asansor1,args=[1])
t5=threading.Thread(target=asansor1,args=[2])
t6=threading.Thread(target=asansor1,args=[3])
t7=threading.Thread(target=asansor1,args=[4])
t8=threading.Thread(target=denetle)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()


"""
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
"""

root.mainloop()
