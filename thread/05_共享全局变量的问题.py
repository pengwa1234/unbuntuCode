from threading import Thread
import time
g_num=0
def work():
    global g_num
    for i in range(1000000):
        g_num+=1
    print("----work中的g_num%s:"%g_num)

def hello():
    global g_num
    for i in range(1000000):
        g_num+=1
    print("---hello--中的g_num:%s"%g_num)

t1=Thread(target=work)
t1.start()
time.sleep(1)

t2=Thread(target=hello)
t2.start()
time.sleep(2)
print("g_num:%s"%g_num)

