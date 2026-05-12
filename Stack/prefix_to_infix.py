def pre_to_in(exp):
    stack = []

    ops = set("+-*/%^")

    for ch in reversed(exp): #prefix traversal: right -> left
        if ch not in ops:
            stack.append(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            """
            here we will pop left operand first, 
            and then right operand
            """

            tmp = "(" + op1 + ch + op2 + ")"

            stack.append(tmp)
    
    return stack[-1] # stack is LIFO based, so the final expression remains at the top of stack