# https://leetcode.com/problems/min-stack/

class MinStack:
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        # 1st element -> value
        # 2nd element -> minmum value
        if not self.stack:
            self.stack.append((x, x))
        else:
            min_val = min(self.stack[-1][1], x)
            self.stack.append((x, min_val))
        
    def pop(self):
        self.stack.pop(-1)
        
    def top(self):
        return self.stack[-1][0]
        
    def getMin(self):
        return self.stack[-1][1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
