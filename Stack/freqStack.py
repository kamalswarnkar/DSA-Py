"""
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

1. FreqStack() constructs an empty frequency stack.
2. push(val) pushes an integer val onto the top of the stack.
3. pop() removes and returns the most frequent element in the stack.

If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
"""

from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.groups = defaultdict(list)
        self.max_freq = 0
        
    def push(self, val: int) -> None:
        self.freq[val] += 1
        f = self.freq[val]

        if f > self.max_freq:
            self.max_freq = f
        
        self.groups[f].append(val)

    def pop(self) -> int:
        x = self.groups[self.max_freq].pop()

        self.freq[x] -= 1

        if not self.groups[self.max_freq]:
            self.max_freq -= 1
        
        return x
            