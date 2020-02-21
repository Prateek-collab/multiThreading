import time
import threading

def square(L):

                for i in L:
                                time.sleep(0.5)
                                print(i**2)

def cube(L):

                for i in L:
                                time.sleep(0.5)
                                print(i**3)


L=[1,2,3,4,5,6,7,8]
t1=threading.Thread(target=square,args=(L,))
t2=threading.Thread(target=cube,args=(L,))

start=time.time()
t1.start()
t2.start()
t1.join()
t2.join()
print(time.time()-start)


