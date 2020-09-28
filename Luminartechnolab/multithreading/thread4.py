import time
from threading import *

def squares(num):
    for i in num:
        time.sleep(1)
        print(i**2,'\n')

def doubles(num):
    for i in num:
        time.sleep(1)
        print(2*i,'\n')

num=[1,2,3,4,5,6]
begin_time=time.time()
print("begin time :",begin_time)
t1=Thread(target=squares,args=(num,)) #arguments are passed as tuples
t1.start()
t2=Thread(target=doubles,args=(num,))
t2.start()
t1.join() #execute main thread only after t1
t2.join() #execute main thread only after t2

end_time=time.time()
print("end time :",end_time)
print("execution time ",end_time-begin_time)