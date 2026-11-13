# using signalling between threads and to ensure that second() waits for first() to finish and third() waits for second() to finish

import threading

class Foo:
    def __init__(self):
        self.event2 = threading.Event()
        self.event3 = threading.Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

        # call event2 and set this
        self.event2.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        self.event2.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

        # signal that second() has finished 
        self.event3.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # wait till everything cleared
        self.event3.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()