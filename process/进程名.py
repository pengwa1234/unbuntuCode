from multiprocessing import Process

def test():
    print(t.name)
    print("----test----")
for i in range(5):
    t=Process(target=test)
    t.start()

