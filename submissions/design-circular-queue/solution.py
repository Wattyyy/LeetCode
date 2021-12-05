# https://leetcode.com/problems/design-circular-queue

from collections import deque
class MyCircularQueue:

    def __init__(self, k: int):
        self.deque = deque([], maxlen=k)
        self.max_size = k
        
    def enQueue(self, value: int) -> bool:
        if len(self.deque) == self.max_size:
            return False
        self.deque.append(value)
        return True
        
    def deQueue(self) -> bool:
        if not self.deque:
            return False
        self.deque.popleft()
        return True
        

    def Front(self) -> int:
        if not self.deque:
            return -1
        return self.deque[0]
        

    def Rear(self) -> int:
        if not self.deque:
            return -1
        return self.deque[-1]

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return len(self.deque) == self.max_size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()