from threading import Thread

import time

def test():
    print("昨晚喝醉了，下次再聊...")
    time.sleep(1)

for i in range(5):
    thread=Thread(target=test)
    thread.start()
print("线程执行完毕！")
