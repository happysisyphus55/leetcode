import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        # create locks
        self.lock_foo = threading.Lock()
        self.lock_bar = threading.Lock()

        # lockbar initially so that foo will run first 
        self.lock_bar.acquire()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            #wait a turn to print "foo"
            self.lock_foo.acquire()
            
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()

            # allow bar to run next 
            self.lock_bar.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            # wait to turn to print "bar"
            self.lock_bar.acquire()
            
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()

            # allow foo to run next 
            self.lock_foo.release()