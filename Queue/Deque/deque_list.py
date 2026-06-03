"""implementing deque using array (list in python)
here, we have used the approach of circular list
which is considered to best approach for the
implementaion of Deque, so far"""

class Deque:
    def __init__(self, cap):
        self.arr = [None] * cap
        self.cap = cap
        self.sz = 0
        self.front = 0
    
    def insertFront(self, val):
        if self.sz == self.cap:
            return None
        
        self.front = (self.front - 1) % self.cap
        self.arr[self.front] = val
        self.sz += 1
    
    def insertRear(self, val):
        if self.sz == self.cap:
            return None
        
        rear = (self.front + self.sz) % self.cap # no '-1' to get the next empty slot in end
        self.arr[rear] = val
        self.sz += 1
    
    def deleteFront(self):
        if self.sz == 0:
            return None
        
        res = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.cap
        self.sz -= 1
        
        return res
    
    def deleteRear(self):
        if self.sz == 0:
            return None
        
        rear = (self.front + self.sz - 1) % self.cap # '-1' so that it dont reah the next empty slot, but the exact rear element exist
        res = self.arr[rear]
        self.arr[rear] = None
        self.sz -= 1
        
        return res
    
    def getFront(self):
        if self.sz == 0:
            return None
        
        return self.arr[self.front]
    
    def getRear(self):
        if self.sz == 0:
            return None
        
        rear = (self.front + self.sz - 1) % self.cap

        return self.arr[rear]

    def isEmpty(self):
        return self.sz == 0

    def size(self):
        return self.sz    