"""
Here we will try to remove
immediate duplicate characters that
appear in the given string
"""

def remove(s):
    stack = []

    for ch in s:
        if not stack: # if stack is empty
            stack.append(ch)
        elif ch != stack[-1]: # if they are not immediate or adjacent duplicates
            stack.append(ch)
        else:
            continue
    
    return "".join(stack) # instead of return the list(stack), it will add all elements to resultant string