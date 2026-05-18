# finding next smaller element for every element using stack

def next_smaller(arr):
    stack = []
    n = len(arr)

    res = [-1] * n

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        
        next_smaller = -1 if len(stack) == 0 else stack[-1]
        res[i] = next_smaller
        stack.append(arr[i])
    
    return res