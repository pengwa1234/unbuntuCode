import queue

q=queue.Queue()
q.put(13,block=True,timeout=5)
q.put_nowait(23)
q.task_done()
print(q.get())
q.join()