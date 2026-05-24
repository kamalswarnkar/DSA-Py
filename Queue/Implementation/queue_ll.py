# implementing Queue using Linked List
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.sz = 0
        self.curr = self.head
        
    def isEmpty(self):
        if self.sz == 0:
            return True
        
        return False

    def enqueue(self, x):
        node = Node(x)
        if self.isEmpty():
            self.curr = self.head = node
        else:
            self.curr.next = node
            self.curr = self.curr.next
        self.sz += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        
        self.head = self.head.next
        self.sz -= 1

        if self.head is None:
            self.curr = None

    def getFront(self):
        if self.sz == 0:
            return -1
        
        return self.head.data

    def size(self):
        return self.sz
