"""
Conversion - From Infix to Prefix or Postfix

1. In infix form, an operator is written in between two operands.
   It is of the form <operand><operator><operand>.
   Eg: A+B 

2. In prefix form, an operator is written before the operands. 
   It is of the form <operator><operand><operand>.
   Eg: +AB

3. In postfix form, an operator is written after the operands.
   It is of the form <operand><operand><operator>.
   Eg: AB+

We'll be using Shunting-Yard Algorithm for the below conversions

For Infix to Postfix:
-------------------------------------------------------------------------
1. Create an empty stack
2. Traverse from left -> right
3. if 'ch' is:
    i.   operand: append to postfix arr
    ii.  '(': Push to stack
    iii. ')': Pop from stack until '(' is found, and append the 
              popped characters into postfix arr
    iv.  operator: If stack is empty -> Push into stack
                   Else, compare with top of stack
                   a. Higher precedence(than stack top) -> Push into stack
                   b. Lower precedence -> Pop from stack until a higher
                      predence is found, and append the popped characters
                      into postfix arr. Then Push 'ch' into stack
4. If still something in stack, pop all, and push into postfix

For Infix to Postfix:
-------------------------------------------------------------------------
1. Create an empty stack
2. Traverse from right -> left
3. if 'ch' is:
    i.   operand: append to prefix arr
    ii.  ')': Push to stack
    iii. '(': Pop from stack until ')' is found, and append the 
              popped characters into prefix arr
    iv.  operator: If stack is empty -> Push into stack
                   Else, compare with top of stack
                   a. Higher precedence(than stack top) -> Push into stack
                   b. Lower precedence -> Pop from stack until a higher
                      predence is found, and append the popped characters
                      into prefix arr. Then Push 'ch' into stack
4. If still something in stack, pop all, and push into prefix
5. reverse the prefix
"""

class Conversion:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.stack = []
        self.postfix = []
        self.prefix = []
        self.precedence = {
            '+' : 1,
            '-' : 1,
            '*' : 2,
            '/' : 2,
            '^' : 3
        }
    
    def isEmpty(self):
        return True if self.top == -1 else False
    
    def peek(self):
        return self.stack[-1]
    
    def push(self, op):
        self.top += 1
        self.stack.append(op)
    
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.stack.pop()
        else:
            return '$'
    
    def isOperand(self, ch):
        return ch.isalpha() or ch.isdigit()
    
    def notGreater(self, i): # only for postfix
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]

            if i == '^':
                return a < b
            
            return True if a <= b else False
        except KeyError:
            return False
    
    def infix_to_postfix(self, exp):
        for i in exp:
            if self.isOperand(i):
                self.postfix.append(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                while (not self.isEmpty()) and self.peek() != '(':
                    a = self.pop()
                    self.postfix.append(a)
                
                if (not self.isEmpty()) and self.peek() != '(':
                    return -1
                else:
                    self.pop()
            else:
                while (not self.isEmpty() and self.notGreater(i)):
                    self.postfix.append(self.pop())
                
                self.push(i)
        
        while not self.isEmpty():
            self.postfix.append(self.pop())

        res = "".join(self.postfix)
        
        self.postfix = [] # to resuse the same object instance if required
        self.stack = [] # to resuse the same object instance if required
        self.top = -1

        return res
    
    def infix_to_prefix(self, exp):
        for ch in reversed(exp):
            if self.isOperand(ch):
                self.prefix.append(ch)
            elif ch == ')':
                self.push(ch)
            elif ch == '(':
                while (not self.isEmpty()) and self.peek() != ')':
                    a = self.pop()
                    self.prefix.append(a)
                
                if (not self.isEmpty()) and self.peek() != ')':
                    return -1
                else:
                    self.pop()
            else:
                while (not self.isEmpty()):
                    top = self.peek()

                    if top == ')':
                        break

                    a = self.precedence[ch]
                    b = self.precedence[top]

                    if a < b or (a == b and ch != '^'): # associativity reverses because traversal is right -> left
                        self.prefix.append(self.pop())
                    else:
                        break
                self.push(ch)

        while not self.isEmpty():
            self.prefix.append(self.pop())
        
        res = "".join(reversed(self.prefix))

        self.prefix = [] # to resuse the same object instance if required
        self.stack = [] # to resuse the same object instance if required
        self.top = -1

        return res
