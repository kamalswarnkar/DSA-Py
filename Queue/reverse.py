# reversing queue elements order
from collections import deque
# iterative approach
def reverse_1(queue): # here, queue is an obj of deque from collections
    stack = []
    
    while queue:
        stack.append(queue.popleft())
    
    while stack:
        queue.append(stack.pop())

# recursive approach
def reverse_2(queue):
    if len(queue) == 0:
        return
    
    x = queue.popleft()
    reverse_2(queue)
    queue.append(x)