from threading import Thread,Lock
import time
def main():
    t1=Thread(target=test1)
    t1.start()
    t2=Thread(target=test2)
    
    t2.start()
    print("main----%s"%g_num)

mutex=Lock()
g_num=0
def test1():
    global g_num
    for i in range(1000000):
        
        mutex.acquire()
        g_num+=1
        mutex.release()
    print("test1----%s"%g_num) 

def test2():
    global g_num
    for i in range(1000000):
        
        mutex.acquire()
        g_num+=1
        mutex.release()
    print("test2----%s"%g_num)

if __name__=="__main__":
    main()
