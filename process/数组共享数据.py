from multiprocessing import Process,Array
import tim

def trans(a,size):
    t=time.datetime()
    for i in range(size):
        print(a[i])
    print("消耗%s"%(time.datetime()-t))

if __name__=='__mian__':
    print("Test share Memory")

    num=10
    a=Array("i",num)

    p=Process(target=trans,args=(a,num))

    p.start()
