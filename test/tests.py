import time
import _thread as thread


def loop1():
    print("loop1现在时间:", time.ctime())
    time.sleep(4)
    print("loop1现在时间:", time.ctime())


def loop2():
    print("loop2现在时间:", time.ctime())
    time.sleep(2)
    print("loop2现在时间:", time.ctime())


def main():
    print("start at :", time.ctime())
    thread.start_new_thread(loop1, ())
    thread.start_new_thread(loop2, ())

    print("wanshile")


if __name__ == '__main__':
    main()
