#Stack implementation using list - gatesmashers
#04.10.26

class stack:
    def __init__(self):
        self.values=[]
    def push(self,x):
        self.values= [x]+ self.values
    def pop(self):
        return self.values.pop(0)
    def peek(self):                         #not in tutorial
        return self.values[0]
    def printstack(self):                   #not in tutorial
        print(self.values)

