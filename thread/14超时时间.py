from threading import Thread,Lock
import time

def test():
	if mutexA.acquire():
		print("A被锁定")
		time.sleep(1)
		res=mutexB.acquire(timeout=4)
		
		if res:
			print("---B在等到被锁定---")
		else:
			mutexA.release()
			time.sleep(0.5)

def task():
	if mutexB.acquire():
		print("B被锁定")
		time.sleep(1)
		if mutexA.acquire():
			print("等待---")
			mutexB.release()

t1=Thread(target=test)
t2=Thread(target=task)

mutexB=Lock()
mutexA=Lock()

t1.start()
t2.start()


