from multiprocessing import Process
import time

g_num=100
def test():
    global g_num
    for i in range(3):
        g_num+=1
        print("多吃点，真好吃。。。")
        time.sleep(1)
        print("test里面的全局变量是%s"%g_num)

for i in range(5):
    p=Process(target=test)
    p.start()
    p.join()
print("全局变量的值：%s"%g_num)


