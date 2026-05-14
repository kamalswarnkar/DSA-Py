# reversing an array in-place using stack

def reverse(arr):
    n = len(arr)
    stack = []

    for i in range(n):
        stack.append(arr[i])
    
    for i in range(n):
        arr[i] = stack.pop()
    
    return arr