from threading import  *
import time
class MyThread(Thread):
    def run(self):
        for i in range(1,10):
            time.sleep(3)
            print(i,'h')
        print(current_thread().getName())
t=MyThread()
t.start()
for i in range(1,10):
    print(i,'h')
print(current_thread().getName())