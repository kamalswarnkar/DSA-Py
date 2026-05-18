# finding previous smaller element for every element using stack

def prev_smaller(arr):
    stack = []
    n = len(arr)

    for i in range(n):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        
        prev_smaller = -1 if len(stack) == 0 else stack[-1]
        print(prev_smaller, end=" ")
        stack.append(arr[i])