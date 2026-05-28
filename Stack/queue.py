# Implementing or creating Queue Data Structure using Stack

"""
Queue Can be implemented by Stack using 3 following Approaches:

1. Enqueue Costly Approach:
    enqueue  -> O(n)
    dequeue  -> O(1)
    space    -> O(n)

2. Dequeue Costly Approach:
    enqueue  -> O(1)
    dequeue  -> O(n)
    space    -> O(n)

3. One Stack Approach: - uses Recursion (recusrion consumes memory)
    enqueue  -> O(1)
    dequeue  -> O(n)
    space    -> O(n) - eliminates the need for a second stack
"""

# Enqueue Costly Approach
class Queue_1:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, val):
        while self.s1:
            self.s2.append(self.s1.pop())
        
        self.s1.append(val)

        while self.s2:
            self.s1.append(self.s2.pop())
    
    def dequeue(self):
        if self.s1:
            return self.s1.pop()
        
        return None
    
    def front(self):
        if self.s1:
            return self.s1[-1]

        return None

    def isEmpty(self):
        return len(self.s1) == 0

    def size(self):
        return len(self.s1)

# Dequeue Costly Approach
class Queue_2:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, val):
        self.s1.append(val)
    
    def dequeue(self):
        if self.s1:
            while len(self.s1) > 1:
                self.s2.append(self.s1.pop())
            
            x = self.s1.pop()

            while self.s2:
                self.s1.append(self.s2.pop())
            
            return x
        
        return None
    
    def front(self):
        if self.s1:
            while len(self.s1) > 1:
                self.s2.append(self.s1.pop())
            
            x = self.s1[-1]

            while self.s2:
                self.s1.append(self.s2.pop())
            
            return x

        return None

    def isEmpty(self):
        return len(self.s1) == 0

    def size(self):
        return len(self.s1)

# implementing queue using only 1 stack
class Queue_3:
    def __init__(self):
        self.s = []

    def enqueue(self, val):
        self.s.append(val)
    
    def dequeue(self):
        if self.s:
            if len(self.s) == 1:
                return self.s.pop()
            
            x = self.s.pop()
            res = self.dequeue()
            self.s.append(x)

            return res
        
        return None
    
    def front(self):
        if self.s:
            if len(self.s) == 1:
                return self.s[-1]
            
            x = self.s.pop()
            res = self.front()
            self.s.append(x)

            return res 

        return None

    def isEmpty(self):
        return len(self.s) == 0

    def size(self):
        return len(self.s)