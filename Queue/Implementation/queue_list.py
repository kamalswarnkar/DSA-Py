# implementing Queue using Array(list in python)
class Queue:
    def __init__(self, n):
        self.queue = []
        self.size = n

    def isEmpty(self):
        return len(self.queue) == 0
    
    def isFull(self):
        return len(self.queue) == self.size
    
    def enqueue(self, x): # adding data/val in end of List
        if self.isFull():
            return "Queue is Full"
        
        self.queue.append(x)
    
    def dequeue(self): # removing dala/val from the front of List in O(n) time
        if self.isEmpty():
            return "Queue is Empty"
        
        self.queue.pop(0)
    
    def getFront(self): # returninng value in front of list
        if not self.isEmpty():
            return self.queue[0]
        
        return -1
    
    def getRear(self): # returninng value in end of list
        if not self.isEmpty():
            return self.queue[-1]
            
        return -1
        