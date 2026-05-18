"""
Here, we will be finding the largest
possible area of rectangle of 1 in a
matrix of 0 and 1.

Approach:
If the height of bars of the histogram is given then 
the largest area of the histogram can be found. This 
way in each row, the largest area of bars of the histogram 
can be found. To get the largest rectangle full of 1’s, 
update the next row with the previous row and find the 
largest area under the histogram, i.e. consider each 1’s as 
filled squares and 0’s with an empty square and consider 
each row as the base.

Time Complexity: O(r * c)
Space Complexity: O(c)

r = no. of Rows
c = no. of Cols
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

def largest_histogram(bars):
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

def largest_rectangle(mat):
    area = largest_histogram(mat[0])
    r = len(mat)
    c = len(mat[0])

    for i in range(1, r):
        for j in range(c):
            if mat[i][j]:
                mat[i][j] += mat[i - 1][j]
        
        area = max(area, largest_histogram(mat[i]))

    return area