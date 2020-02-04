# https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:
    
    def __init__(self, k):
        self.queue = []
        self.max = k
        self.rear = -1
        self.front = -1
        
        
    def enQueue(self, value):
        if len(self.queue) == self.max:
            return False
        if not self.queue:
            self.queue.append(value)
            self.rear = value
            self.front = value
            return True
        else:
            self.queue.append(value)
            self.rear = value
            return True        
  

    def deQueue(self):
        if not self.queue:
            return False
        if len(self.queue) == 1:
            self.queue.pop(0)
            self.rear = -1
            self.front = -1
            return True
        else:
            self.queue.pop(0)
            self.front = self.queue[0]
            return True

        
    def Front(self):
        return self.front
    
    
    def Rear(self):
        return self.rear

    
    def isEmpty(self):
        return not self.queue
        

    def isFull(self):
        return len(self.queue) == self.max
