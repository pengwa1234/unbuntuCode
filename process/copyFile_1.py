from multiprocessing import Pool,Manager
import os
import time

def copyFile(name,oldFileName,newFileName,queue):
    print("read file start")
    fr=open(oldFileName+os.sep+name,"r")
    content=fr.read()
    fw=open(newFileName+os.sep+name,"w")
    print("write file start")
    fw.write(content)
    queue.put(name)
    fr.close()
    fw.close()

def main():

    oldFileName=input("请输入旧的文件夹名字：") 
    newFileName=oldFileName+"复件"
    #print(newFileName)
    os.mkdir(newFileName)

    filenames=os.listdir(oldFileName)
    print(filenames)
    pool=Pool(5)
    queue=Manager().Queue()
    for name in filenames:
        print("文件名是%s"%name)
        pool.apply_async(copyFile,args=(name,oldFileName,newFileName,queue))
    pool.close()
    
    allNums=len(filenames)
    num=0
    while True:
        queue.get()
        num+=1
        copyrate=num/allNums*100
        print("\r%.2f%%"%copyrate)
        time.sleep(0.01)
        if num==allNums:
            break
    print("copy完成...")

if __name__=="__main__":
    main()
