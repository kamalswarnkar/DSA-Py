"""
Generating 1st 'n' numbers from the given numbers only
where all the numbers will be in inreasing order, and
will consist of only digits which are given.

This is a BFS kind of problem where queue is used for
Breadth-First Generation of numbers in increasing order
of their length and magnitude.
"""

from collections import deque as dq

def genFirstN_1(n): # here, we are using only 2 digits: 5, 6
    queue = dq()

    queue.append("5")
    queue.append("6")

    for i in range (n):
        curr = queue.popleft()
        print(curr, end=" ")
        queue.append(curr + "5")
        queue.append(curr + "6")

def genFirstN_2(n):
    queue = dq()

    queue.append("5")
    queue.append("6")

    i = 0

    while (i + len(queue)) < n:
        curr = queue.popleft()
        print(curr, end=" ")
        queue.append(curr + "5")
        queue.append(curr + "6")
        i += 1
    
    while i < n:
        print(queue.popleft(), end=" ")
        i += 1