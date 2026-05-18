"""
Here, we will be finding the largest
possible area of histogram consisting
of adjacent bars of width = 1 unit, and 
variable height.

Approach:
1. initialize area = 0
2. find previous smaller element's index for every element/bar
3. find next smaller element's index for every element/bar
4. Do the following:
    curr = bars[i]
    curr += (i - ps[i] - 1)*bars[i]
    curr += (ns[i] - i - 1)*bars[i]
    area = max(area, curr)
5. return area

Time Complexity: O(n)
Space Complexity: O(n)
"""

def prev_smaller(arr):
    stack = []
    n = len(arr)

    ps = [-1] * n

    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        
        ps[i] = -1 if len(stack) == 0 else stack[-1]
        stack.append(i)
    
    return ps

def next_smaller(arr):
    stack = []
    n = len(arr)

    ns = [n] * n

    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        
        next_smaller = n if len(stack) == 0 else stack[-1]
        ns[i] = next_smaller
        stack.append(i)
    
    return ns

def largest_area(bars):
    area = 0
    ps = prev_smaller(bars)
    ns = next_smaller(bars)
    n = len(bars)

    for i in range(n):
        """
        curr = bars[i]
        curr += (i - ps[i] - 1)*bars[i]
        curr += (ns[i] - i - 1)*bars[i]
        """
        curr = bars[i] * (ns[i] - ps[i] - 1)
        area = max(area, curr)
    
    return area
