from threading import Thread,Lock
import time

class Read_data(Thread):
	def run(self):
		while True:
			time.sleep(0.1)
			mutex.acquire()
			print("---读数据中---")
			f=open("data.txt","r")
			content=f.read()
			print(content)
			mutex.release()


class Write_data(Thread):
		def run(self):
			while True:
				mutex.acquire()
				print("----写数据中----")
				f=open("data.txt","w")
				f.write("hello python 2020!")
				f.close()
				mutex.release()
				time.sleep(0.1)

mutex=Lock()

t1=Read_data()
t2=Write_data()

t1.start()
t2.start()



