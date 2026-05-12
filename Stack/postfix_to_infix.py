def post_to_in(exp):
    stack = []
    ops = set("+-*/%^")

    for ch in exp: #postfix traversal: left -> right
        if ch not in ops:
            stack.append(ch)
        else:
            op2 = stack.pop()
            op1 = stack.pop()

            """
            in postfix the order of getting operand changes 
            unlike in prefix, 
            where we take op1 first, and then op2
            but here we will pop right operand first, and then left operand
            """

            tmp = "(" + op1 + ch + op2 + ")"
            stack.append(tmp)
        
    return stack[-1] # stack is LIFO based, so the final expression remains at the top of stack