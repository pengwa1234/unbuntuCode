import threading

NUM = 0
local = threading.local()

def run(x, n):
   x = x + n
   x = x - n
 
def func(n):
  local.x = NUM  # 将全局变量赋值给一个线程要执行的函数的局部变量。
  for i in range(1000000):
  	run(local.x, n)
  	
  print('%s-%d' % (threading.current_thread().name, local.x))


if __name__ == '__main__':
     t1 = threading.Thread(target=func, args=(6,))
     t2 = threading.Thread(target=func, args=(9,))
     t1.start()
     t2.start()
     t1.join()
     t2.join()
     print('NUM = ', NUM)