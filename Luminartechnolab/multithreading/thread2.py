from threading import *
import  time
def display():

    for i in range(1,10):
        time.sleep(5)
        print("child thread executing")
    print(current_thread().getName())
t=Thread(target=display)
t.start()

for i in range(1,10):
    time.sleep(5)
    print("main thread executing")
print((current_thread().getName()))