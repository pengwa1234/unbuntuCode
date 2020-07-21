# from threading import Thread
import threading

class Student():
	def __init__(self,name):
		self.name=name

dic={}

def process_student(name):
	std=Student(name)
	dic[threading.current_thread().name]=std
	print('process_student',std.name)

	do_task_1()
	do_task_2()

def do_task_1():
	std=dic[threading.current_thread().name]
	print('do_task_1',std.name)
	do_subtask_1()

def do_task_2():
	std=dic[threading.current_thread().name]
	print("do_task_2",std.name)
	do_subtask_2()

def do_subtask_1():
	std=dic[threading.current_thread().name]
	print("do_subtask_1", std.name)

def do_subtask_2():
	std=dic[threading.current_thread().name]
	print("do_subtask_2", std.name)


if __name__ == '__main__':
    t1 = threading.Thread(target=process_student,args=('小明',))
    t2 = threading.Thread(target=process_student,args=('铁蛋',))
    t1.start()
    t2.start()