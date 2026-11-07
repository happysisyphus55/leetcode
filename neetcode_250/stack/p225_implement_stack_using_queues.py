# making the push costly
# newest element is always sitting at the front of the main queue, perfectly mimicking a stack's top

from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)

        # move all the elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        if self.empty():
            # for empty stack return an error
            raise IndexError("pop from an empty stack")

        # remove an return the front element of q1
        return self.q1.popleft()

    def top(self) -> int:
        if self.empty():
            raise IndexError("top from an empty stack")

        # return the front element of q1 without removing it
        return self.q1[0]

    def empty(self) -> bool:
        # if q2 is empty, then the stack is empty
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
