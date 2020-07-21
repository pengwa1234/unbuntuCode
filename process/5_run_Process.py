from multiprocessing import Process
import os, time, random

def r():
    print('run method')
            
if __name__ == "__main__":
    print("main process run...")
     #没有指定Process的targt
    p1 = Process()
    p2 = Process()
 #如果在创建Process时不指定target，那么执行时没有任何效果。因为默认的run方法是判断如果不指定target，那就什么都不做
#所以这里手动改变了run方法                                      
    p1.run = r  
    p2.run = r
    p1.start()                                          
    p1.join()
    
    p2.start()
    p2.join()                                           
    print ("main process runned all lines...")
