from multiprocessing import Queue,Process
import time,os,random

def write(q):
    for i in ["A","B","C"]:
        q.put(i)
        time.sleep(random.random())
        print("write的pid是：%s"%os.getpid())

def read(q):
    while True:
        if not q.empty():
            value=q.get()
            print("Get %s from queue.read的pid是%s"%(value,os.getpid()))
            time.sleep(random.random())
        else:
            break


if __name__=="__main__":
    q=Queue()
    pw=Process(target=write,args=(q,))
    
    pr=Process(target=read,args=(q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
    print("主函数的pid:",os.getpid())
    print("程序执行中----")

    print("数据写入完毕！")
