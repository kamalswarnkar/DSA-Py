# Implementing or creating Stack Data Structure using Queue
from collections import deque as dq

"""
Stack Can be implemented by Queue using 3 following Approaches:

1. Push Costly Approach:
    push  -> O(n)
    pop   -> O(1)
    space -> O(n)

2. Pop Costly Approach:
    push  -> O(1)
    pop   -> O(n)
    space -> O(n)

3. One Queue Approach: - more optimal
    push  -> O(n)
    pop   -> O(1)
    space -> O(1) - (auxiliary space), eliminates the need for a second queue
"""

# Push Costly Approach
class Stack_1:
    def __init__(self):
        self.q1 = dq() # to store actual items
        self.q2 = dq() # to be used as an auxiliary queue
    
    def push(self, val):
        """
        1. enqueue val in q2
        2. shift all values from q1 -> q2
        3. swap q1, and q2
        """
        self.q2.append(val)
        while self.q1:
            self.q2.append(self.q1.popleft())
        
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self):
        if self.q1:
            return self.q1.popleft()
        
        return None
    
    def top(self):
        if self.q1:
            return self.q1[0]
        return None
    
    def isEmpty(self):
        return len(self.q1) == 0
    
    
    def size(self):
        return len(self.q1)

# Pop Costly Approach
class Stack_2:
    def __init__(self):
        self.q1 = dq() # to store actual items
        self.q2 = dq() # to be used as an auxiliary queue
    
    def push(self, val):
        self.q1.append(val)
    
    def pop(self):
        if self.q1:
            while len(self.q1) > 1: # leaving 1 element in q1 and pushing others in q2, to later return as popped element
                self.q2.append(self.q1.popleft())
            
            x = self.q1.popleft()
            self.q1, self.q2 = self.q2, self.q1

            return x
        
        return None
    
    def top(self):
        if self.q1:
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
            
            x = self.q1.popleft()
            self.q2.append(x)

            self.q1, self.q2 = self.q2, self.q1

            return x
        
        return None
    
    def isEmpty(self):
        return len(self.q1) == 0
    
    
    def size(self):
        return len(self.q1)

# implementing stack using only 1 queue
class Stack_3:
    def __init__(self):
        self.q = dq() # only single queue
    
    def push(self, val):
        s = len(self.q) # getting previos length/size of queue

        self.q.append(val)

        """
        1. Popping all prev elements
        2. append them after current - that's why using previous size of queue 
        """
        for _ in range(s):
            self.q.append(self.q.popleft())
    
    def pop(self):
        if self.q:
            return self.q.popleft()
        
        return None
    
    def top(self):
        if self.q:
            return self.q[0]
        
        return None
    
    def isEmpty(self):
        return len(self.q) == 0
    
    
    def size(self):
        return len(self.q)
    