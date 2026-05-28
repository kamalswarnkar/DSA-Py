# implementing Queue using Circular List

class Queue:
    def __init__(self, cap):
        self.arr = [None] * cap
        self.cap = cap
        self.sz = 0
        self.front = 0

    def enqueue(self, val):
        if self.sz == self.cap:
            return "Queue is already Full"
        else:
            rear = (self.front + self.sz - 1) % self.cap
            rear = (rear + 1) % self.cap
            self.arr[rear] = val
            self.sz += 1
    
    def dequeue(self):
        if self.sz == 0:
            return "Queue is already Empty"
        else:
            res = self.arr[self.front]
            self.arr[self.front] = None
            self.front = (self.front + 1) % self.cap
            self.sz -= 1
            return res
    
    def getFront(self):
        if self.sz == 0:
            return None
        else:
            return self.arr[self.front]
    
    def getRear(self):
        if self.sz == 0:
            return None
        else:
            rear = (self.front + self.sz - 1) % self.cap
            return self.arr[rear]
    
    def isEmpty(self):
        return self.sz == 0
    
    def isFull(self):
        return self.sz == self.cap

    def size(self):
        return self.sz
    