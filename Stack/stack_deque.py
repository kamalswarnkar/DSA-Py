"""
implementation of stack using Deque.

Deque is preferred over the list in the cases 
where we need quicker append and pop operations 
from both the ends of the container, as deque 
provides an O(1) time complexity for append and pop 
operations as compared to list which provides 
O(n) time complexity. 
"""

from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Stack is Empty")
            return None

    def display(self):
        if not self.stack:
            print(-1)
            return
        
        for val in self.stack:
            print(val, end=" ")
        
        print()