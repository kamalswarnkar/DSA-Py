# implementing deque using linked list (doubly linked list)

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.sz = 0
    
    def size(self):
        return self.sz
    
    def isEmpty(self):
        return self.sz == 0
    
    def insertFront(self, val):
        tmp = Node(val)

        if self.front is None:
            self.front = self.rear = tmp
        else:
            self.front.prev = tmp
            tmp.next = self.front
            self.front = tmp
        
        self.sz += 1

    def insertRear(self, val):
        tmp = Node(val)
        
        if self.rear is None:
            self.front = tmp
        else:
            self.rear.next = tmp
            tmp.prev = self.rear

        self.rear = tmp
        self.sz += 1
    
    def deleteFront(self):
        if self.front is None:
            return None
        else:
            res = self.front.key
            self.front = self.front.next

            if self.front is None:
                self.rear = None
            else:
                self.front.prev = None
            
            self.sz -= 1

            return res
    
    def deleteRear(self):
        if self.rear is None:
            return None
        else:
            res = self.rear.key
            self.rear = self.rear.prev

            if self.rear is None:
                self.front = None
            else:
                self.rear.next = None
            
            self.sz -= 1

            return res
    
    def getFront(self):
        if self.front:
            return self.front.key
        return None
    
    def getRear(self):
        if self.rear:
            return self.rear.key
        return None
    