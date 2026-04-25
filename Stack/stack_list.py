# implementation of stack using List(Array)

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Stck is Empty")
    
    def display(self):
        if self.stack:
            for i in range(len(self.stack)):
                print(self.stack[i], end = " ")
            
            print()
        else:
            print(-1)