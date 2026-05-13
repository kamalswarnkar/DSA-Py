"""
We'll implement the 'k' number
of stacks in a single array,
for storing the elements.

All 'k' stacks will use same
array, to optimally use the space.
"""

class kStacks:
    def __init__(self, n, k):
        self.size = n # size of array
        self.k = k # no of stacks
        self.arr = [None] * n # array initialized
        self.top = [-1] * k # contains top of eack stack, initialized with -1, initially
        self.next = [(i+1) for i in range(n)] 
        """
        maintainng next element of top(element just below the 
        top elementof stack) or point to free space
        """
        self.next[n - 1] = -1 # last element  = -1, it shows that there is no free space or next element available after the last element
        self.freespot = 0 # this varibale will help us deal with 'next' array
    
    def push(self, sn, val):
        #1. check for overflow condition
        if self.freespot == -1:
            return False
        
        #2. find index to push the the 'val'
        idx = self.freespot

        #3. insert element into the array
        self.arr[idx] = val

        #4. update freespot
        self.freespot = self.next[idx]

        #5. update 'next' array
        self.next[idx] = self.top[sn - 1] # '0' based indexing

        #6. update 'top' array
        self.top[sn - 1] = idx

        return True
    
    def pop(self, sn):
        #1. check for underflow condition
        if self.top[sn - 1] == -1:
            return -1
        
        #2. find index
        idx = self.top[sn - 1]

        #3. update 'top' array to remove/pop the previous top
        self.top[sn - 1] = self.next[idx]
        x = self.arr[idx]
        self.arr[idx] = None

        #4. update 'next' array
        self.next[idx] = self.freespot

        #5. update freespot
        self.freespot = idx

        return x
    
    def isEmpty(self, sn):
        return self.top[sn - 1] == -1