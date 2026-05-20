class Conversion:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.stack = []
        self.output = []
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
    
    def notGreater(self, i):
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
                self.output.append(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                while (not self.isEmpty()) and self.peek() != '(':
                    a = self.pop()
                    self.output.append(a)
                
                if (not self.isEmpty()) and self.peek() != '(':
                    return -1
                else:
                    self.pop()
            else:
                while (not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                
                self.push(i)
        
        while not self.isEmpty():
            self.output.append(self.pop())
        
        return "".join(self.output)
    