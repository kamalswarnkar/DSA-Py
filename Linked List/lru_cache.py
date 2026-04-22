"""
LRU (Least Recently Used) Cache -> A data Structure or a memory mgmt algo
that discards the least recently accessed item when the cache reached the capacity
"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:
      
    def __init__(self, cap):
        #code here
        self.cap = cap
        self.cache = {}
        
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node

    def get(self, key):
        #code here
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        
        self.remove(node)
        self.insert(node)
        
        return node.val

    def put(self, key, val):
        #code here
        
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, val)
        
        self.cache[key] = node
        
        self.insert(node)
        
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]