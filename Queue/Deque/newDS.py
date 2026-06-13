"""
Here we will design a new Data Structure,
a SpecialQueue which supports following 
operations enqueue, deque, getMin() or 
getMax() where getMin() operation takes 
O(1) time.

The idea is to use Doubly ended Queue to 
store in increasing order if the structure 
is to return the minimum element and store 
in decreasing order if the structure is to 
return the maximum element. 
"""

from collections import deque as dq

class SpecialQueue:
    def __init__(self):
        self.Q = dq([]) # Queue to store the element to maintain the order of insertion
        self.D = dq([]) # Doubly ended queue to get the minimum element in the O(1) time
    
    def enqueue(self, val):
        if len(self.Q) == 0:
            self.Q.append(val)
            self.D.append(val)
        else:
            self.Q.append(val)

            while(self.D and self.D[-1] > val):
                self.D.pop()
            
            self.D.append(val)
    
    def dequeue(self):
        if self.Q[0] == self.D[0]:
            self.Q.popleft()
            self.D.popleft()
        else:
            self.Q.popleft()
    
    def getMin(self):
        return self.D[0]