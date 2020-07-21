from threading import Thread,Lock
import time
def main():
    t1=Thread(target=test1)
    t1.start()
    t2=Thread(target=test2)
    
    t2.start()

def test1():
    print()
    g_num=0
    g_num+=1
    print("test1----%s"%g_num) 

def test2():
    g_num=100
    print("test2----%s"%g_num)

if __name__=="__main__":
    main()
