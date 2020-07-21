from threading import Thread
import time

g_num=0
g_flag=1
def test1():
    global g_num
    global g_flag
    if g_flag==1:
        for i in range(1000000):
            g_num+=1
        g_flag=0
        print("test1----%s"%g_num) 

def test2():
    global g_num
    #轮询一直做判断a_flag什么时候等于0
    while True:
        if g_flag==0:
            for i in range(1000000):
                g_num+=1
            print("test2----%s"%g_num)
            break

def main():
    t1=Thread(target=test1)
    t1.start()
    t2=Thread(target=test2)
    
    t2.start()
    print("main----%s"%g_num)


if __name__=="__main__":
    main()
