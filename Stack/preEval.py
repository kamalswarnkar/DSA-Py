"""
A prefix expression evaluation

1. traverse from right-< left

2. check each char:
    i. if char is digit -> push into stack
    ii. else, pop latest 2 numbers from stack, 
    and evaluate them according to the new char appeared
"""

def prefix_evaluate(exp):
    stack = []

    for ch in reversed(exp):
        if ch[0].isdigit() or (len(ch) > 1 and ch[0] == '-'):
            stack.append(int(ch))
        else:
            a = int(stack.pop())
            b = int(stack.pop())

            if ch == "+":
                stack.append(a + b)
            elif ch == "-":
                stack.append(a - b)
            elif ch == "*":
                stack.append(a * b)
            elif ch == "/":
                stack.append(a // b)
            elif ch == "^":
                stack.append(a ** b)
    
    return stack[-1]