import queue

q=queue.Queue(3)
q.put(13,block=True,timeout=5)
q.task_done()
q.put_nowait(23)
q.task_done()
print(q.get())
q.join()