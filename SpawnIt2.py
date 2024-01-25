from multiprocessing import Process
import time


def square(numbers):
    #time.sleep(10)
    #tFile = open("C:\\Users\\carolyn.brodie\\Desktop\\Multiprocessing\\out1.txt", "w")
    tFile = open("out1.txt", "w")
    for x in numbers:
        tFile.write("The number squared is " + str(x*x) + "\n")
    tFile.close()


def is_even(numbers):
    #time.sleep(10)
    #tFile = open("C:\\Users\\carolyn.brodie\\Desktop\\Multiprocessing\\out2.txt", "w")
    tFile = open("out2.txt", "w")
    for x in numbers:
        if x % 2 == 0:
            tFile.write(str(x) + " is an even number\n");
    tFile.close()


if __name__ == '__main__':
    numbers = [43, 50, 5, 98, 34, 35, 2]

    p1 = Process(target=square, args=(numbers,))
    p2 = Process(target=is_even, args=(numbers,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")
