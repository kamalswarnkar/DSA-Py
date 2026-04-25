"""
Implementing Stack using Singly List
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.head = None
        self.sz = 0
    
    def push(self, val):
        tmp_node = Node(val)
        tmp_node.next = self.head
        self.head = tmp_node
        self.sz += 1
    
    def size(self):
        return self.sz
    
    def peek(self):
        if self.head is None:
            return None
        
        return self.head.data
    
    def pop(self):
        if self.head is None:
            return None
        
        res = self.head.data
        self.head = self.head.next
        self.sz -= 1

        return res
    
    def display(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end=" ")
            tmp = tmp.next
        print()
    
    def is_Empty(self):
        return self.sz == 0