# https://leetcode.com/problems/print-in-order

from threading import Lock

class Foo:
    def __init__(self):
        self.job1 = Lock()
        self.job2 = Lock()
        self.job1.acquire()
        self.job2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.job1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.job1:
        # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.job2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self.job2:
            printThird()