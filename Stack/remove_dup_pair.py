"""
Here we will try to remove
immediate duplicate pairs of characters that
appear in the given string
"""

def remove_pair(s):
    stack = []

    for ch in s:
        if not stack: # if stack is empty:
            stack.append(ch)
        elif ch == stack[-1]: # if the immediate duplicate pair appears
            stack.pop()
        else:
            stack.append(ch)
    
    if not stack: # if all the pairs are removed and the stack becomes empty after it
        return "Empty String"
    
    return "".join(stack) # instead of return the list(stack), it will add all elements to resultant string