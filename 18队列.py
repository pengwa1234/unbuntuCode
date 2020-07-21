import queue
from multiprocessing import Queue

# 只能放我5个
q = Queue(5)
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
print('******')
try:
    # 满了的话我也不等
    q.put_nowait(6)
    print('######')
except queue.Full:
    print('队列溢出，做点别的处理')
    pass

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
try:
    # 空了的话数据我就不取了
    print("如果空了就直接跳过")
    print(q.get_nowait())
except queue.Empty:
    pass