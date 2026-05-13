"""
A data structure that represents 2 stacks
that are implemented using 1 single array
for storing the elements.

Both the stacks use same array dynamically,
which leads to optimal space utilization.
"""

class twoStack:
    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = n
    
    def push1(self, val):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = val
            return True
        
        return False
    
    def push2(self, val):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = val
            return True
        
        return False
    
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.arr[self.top1] = None
            self.top1 -= 1
            return x
        
        return None
    
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.arr[self.top2] = None
            self.top2 += 1
            return x
        
        return None
    
    def peek1(self):
        if self.top1 >= 0:
            return self.arr[self.top1]
        
        return None
    
    def peek2(self):
        if self.top2 < self.size:
            return self.arr[self.top2]
        
        return None
    
    def isEmpty1(self):
        return self.top1 == -1
    
    def isEmpty2(self):
        return self.top2 == self.size

    def size1(self):
        return self.top1 + 1
    
    def size2(self):
        return self.size - self.top2
        