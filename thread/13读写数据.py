from threading import Thread,Lock
import time

class Read_data(Thread):
	def run(self):
		while True:
			if lock1.acquire():
				print("---读数据中---")
				f=open("data.txt","r")
				content=f.read()
				print(content)
				lock2.release()


class Write_data(Thread):
		def run(self):
			while True:
				if lock2.acquire():
					print("----写数据中----")
					f=open("data.txt","w")
					f.write("hello python 2020!")
					f.close()
					lock1.release()

lock1=Lock()
lock2=Lock()

lock1.acquire()

t1=Read_data()
t2=Write_data()

t1.start()
t2.start()



