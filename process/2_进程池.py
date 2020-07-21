from multiprocessing import Pool
import os 
import time

def test():
    for i in range(5):
        print("---%s----"%i)
        time.sleep(1)

pool=Pool(5)

for i in range(10):
    pool.apply_async(test)


pool.close()

pool.join()
