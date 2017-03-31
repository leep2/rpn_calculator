
# coding: utf-8

class RpnCalc():
    
    def __init__(self):
        self.stack = []
        
    def add_to_stack(self, inpt):
        self.stack.append(inpt)

    def swap(self):
        a, b = self.remove_from_stack()
        self.add_to_stack(b)
        self.add_to_stack(a)

    def remove_from_stack(self):
        b = self.stack.pop()
        a = self.stack.pop()
        return a, b
        
    def operation(self, inpt):
        a, b = self.remove_from_stack()
        if inpt == '+':
            result = a + b
        elif inpt == '-':
            result = a - b
        elif inpt == '*':
            result = a * b
        elif inpt == '/':
            result = a / b
        self.add_to_stack(result)
        
    def run(self):
        inpt = raw_input(': ')
        while inpt != 'q':
            if inpt in ['+', '-', '*', '/']:
                self.operation(inpt)
            elif inpt == 'c':
                self.__init__()
            elif inpt == 'swap':
                self.swap()
            else:
                self.add_to_stack(float(inpt))
            print self.stack
            inpt = raw_input(': ')
