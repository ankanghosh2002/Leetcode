# Reverse a string using Stack
# Write a function in python that can reverse a string using stack.
#04.10.26



import StackDeque

s = StackDeque.stack()

sentence = "We will conquere COVID-19"
rev_sentence = ''

for char in sentence:
    s.push(char)

while not s.is_empty():
    rev_sentence += s.pop()

print(rev_sentence)


def reverse_string(s):
    stack = StackDeque.stack()

    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()

    return rstr

'''
import StackDeque

s=StackDeque.stack()

sentence= "We will conquere COVID-19"
rev_sentence=''

for i in sentence:
    s.push(i)

for i in range(s.size()):
    rev_sentence+=s.pop()

print(rev_sentence)
'''
