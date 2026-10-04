#Stack implementation using Deque - codebasics
#04.10.26
from collections import deque

class stack:
    def __init__(self):
        self.values=deque()
    def push(self,x):
        self.values.append(x)
    def pop(self):
        return self.values.pop()
    def peek(self):                         
        return self.values[-1]
    def printstack(self):                   #not in tutorial
        print(self.values)
    def is_empty(self):
        return len(self.values)==0
    def size(self):
        return len(self.values)

