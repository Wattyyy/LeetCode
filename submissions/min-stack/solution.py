# https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.min_stack = []

    def push(self, x):
        if len(self.min_stack) == 0:
            self.min_stack.append((x, x))
            return
        elif x < self.min_stack[-1][1]:
            self.min_stack.append((x, x))
        else:
            min_val = self.min_stack[-1][1]
            self.min_stack.append((x, min_val))


    def pop(self):
        self.min_stack.pop(-1)
        

    def top(self):
        return self.min_stack[-1][0]

        
    def getMin(self):
        return self.min_stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()