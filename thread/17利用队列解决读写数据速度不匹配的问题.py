from threading import Thread
import time
from queue import Queue

class Read_data(Thread):
	def run(self):
		while True:
			if not q.empty():
				print("---读数据中---")
				q.get()



class Write_data(Thread):
	def run(self):
		self.num=0
		while True:
			if not q.full():
				self.num+=1
				print("----写数据中----",self.num)
				q.put("hello python,2020!")

q=Queue(500)

t1=Read_data()
t2=Write_data()

t1.start()
t2.start()



