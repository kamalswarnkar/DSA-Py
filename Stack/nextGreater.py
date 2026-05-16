# finding next greater element for every element using stack

def next_greater(arr):
    stack = []
    n = len(arr)

    res = [-1] * n

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        next_greater = -1 if len(stack) == 0 else stack[-1]
        res[i] = next_greater
        stack.append(arr[i])
    
    return res