def pre_to_in(exp):
    stack = []

    ops = set("+-*/%^")

    for ch in reversed(exp):
        if ch not in ops:
            stack.append(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()

            tmp = "(" + op1 + ch + op2 + ")"

            stack.append(tmp)
    
    return stack[-1]