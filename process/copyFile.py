from multiprocessing import Pool
import os
import time

def copyFile(name,oldFileName,newFileName):
    print("read file start")
    fr=open(oldFileName+os.sep+name,"r")
    content=fr.read()
    fw=open(newFileName+os.sep+name,"w")
    print("write file start")
    fw.write(content)
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

    for name in filenames:
        print("文件名是%s"%name)
        pool.apply_async(copyFile,args=(name,oldFileName,newFileName))
    pool.close()
    pool.join()

if __name__=="__main__":
    main()
