'''
Initialize  a Stack for operators, output list
Split the input into a list of tokens.
for each token (left to right):
       if it is operand:  append to output
       if it is '(': push onto Stack
       if it is ')': pop & append till '('
       if it in '+-*/': 
         while peek has precedence >= it:
            pop & append
         push onto Stack
    pop and append the rest of the Stack.
'''

from pyliststack import Stack

#input = "(((A+B)*(C-E))/(F+G))"
#input = "A*B+C/D"
#input = "A*(B+C)/D"
#input = "A*(B+C/D)"
#input = "((A * B) +(C / D))"
input = "A * (B + C) / D"
output = ""

stack = Stack()

def getpri(c):
    if c == '(' or c == ')':
        return 1
    if c == '+' or c == '-':
        return 2
    if c == '*' or c == '/':
        return 3
    return 0

print input

for ch in input:
    if ch >= 'A' and ch <= 'Z':
        output += ch
    if ch == '(':
        stack.push(ch) 
    if ch == ')':
        while not stack.isEmpty():
            cur = stack.pop()
            if cur == "(":
                break        
            output += cur
    if ch in ('+', '-', '*', '/'):
        while not stack.isEmpty():
            if getpri(stack.peek()) >= getpri(ch):
                output += stack.pop()
            else:
                break
        stack.push(ch)

    #if not stack.isEmpty():
        #print "stack: "
        #stack.show()

while not stack.isEmpty():
    output += stack.pop()

print output
