from threading import Thread
import time

li=[11,22,33]
def test(num):
    li.append(num)
    print(li)
    time.sleep(1)

for i in range(5):
    t=Thread(target=test,args=(55,))

    t.start()
    time.sleep(1)

print("主进程：",li)


