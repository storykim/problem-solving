s = input()

expr_stack = []
op_stack = []

for c in s:
    if c.isalpha():
        expr_stack.append(c)
    elif c == '(':
        op_stack.append(c)
    elif c == ')':
        while op_stack[-1] != '(':
            expr_stack.append(op_stack.pop())
        op_stack.pop()
    elif c in ['+', '-']:
        while op_stack and op_stack[-1] in ['+', '-', '*', '/']:
            expr_stack.append(op_stack.pop())
        op_stack.append(c)
    else:
        while op_stack and op_stack[-1] in ['*', '/']:
            expr_stack.append(op_stack.pop())
        op_stack.append(c)

while op_stack:
    expr_stack.append(op_stack.pop())
print(''.join(expr_stack))

