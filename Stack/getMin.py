"""
We'll be using stack to implement
the get_min fn which gets the min
val present in stack at the moment
in O(1) time complexity

Time Complexity: O(1)
Space Complexity: O(n)
"""

class Stack:
    def __init__(self):
        self.stack = []
        self.aux_stack = [float('inf')]
    
    def push(self, val):
        self.stack.append(val)
        if val <= self.aux_stack[-1]:
            self.aux_stack.append(val)
    
    def pop(self):
        if self.stack:
            if self.stack[-1] == self.aux_stack[-1]:
                self.aux_stack.pop()

            return self.stack.pop()

    
    def size(self):
        return len(self.stack)
    
    def get_min(self):
        if len(self.aux_stack) > 1:
            return self.aux_stack[-1]
        
        return None
    