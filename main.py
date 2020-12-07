import threading
import os

def asansor1():
    print("1. Asansör threadi: {}".format(threading.current_thread().name)) 
    print("1. Asansörün ID'si: {}".format(os.getpid())) 

def asansor2():
    print("2. Asansör threadi: {}".format(threading.current_thread().name)) 
    print("2. Asansörün ID'si: {}".format(os.getpid())) 


if __name__ == "__main__": 
  
    # print ID of current process 
    print("Programın ID'si: {}".format(os.getpid())) 
  
    # print name of main thread 
    print("Main thread adı: {}".format(threading.current_thread().name)) 
  
    # creating threads 
    a1 = threading.Thread(target=asansor1, name='a1') 
    a2 = threading.Thread(target=asansor2, name='a2')   
  
    # starting threads 
    a1.start() 
    a2.start() 
  
    # wait until all threads finish 
    a1.join() 
    a2.join() 