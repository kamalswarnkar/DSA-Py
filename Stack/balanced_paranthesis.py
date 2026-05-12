"""
Here, i will write a program which will take a string
of parathesis, and it will check whether it is in
proper order or not, or whether it is valid or not!
"""

def is_matching(a, b): # helps in matching whether the closing and opening brackets are corresponding or not
    # if (a == '(' and b == ')') or (a == '{' and b == '}') or (a == '[' and b == ']'):
    #     return True

    pairs = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    
    return a == pairs[b]

def is_balanced(s):
    stack = []

    opening = {'(', '{', "["} # we used set instead of list, as it has faster lookup than list

    for ch in s:
        if ch in opening:
            stack.append(ch)
        else:
            if not stack: # if a closing bracket appears before opening one
                return False
            
            elif not is_matching(stack[-1], ch): # if closing bracket doesnt match with last opening one
                return False
            else: # if closing bracket match with last opening one 
                stack.pop()
            """
            the correct order is that, the closing brakcet which appears 
            must be corresponding to the last opening bracket, otherwise
            it will not be valid.
            """
    """
    if stack still not empty, then it must be invalid, 
    as all valid pair of open and close bracket will pop 
    or disappear.
    """
    return len(stack) == 0 
        
            