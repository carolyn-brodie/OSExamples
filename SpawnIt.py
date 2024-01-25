from multiprocessing import Process
import time
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def greeting(name, sleep_time):
    info('function greeting')
    time.sleep(sleep_time);
    print('hello' + " " + name)


if __name__ == '__main__':
    info("main line")
    p1 = Process(target=greeting, args=('world',5,))
    p2 = Process(target=greeting, args=('friend',10,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
