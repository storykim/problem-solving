s = input()
bomb = input()

stack = []
for c in s:
    stack.append(c)
    if ''.join(stack[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if not stack:
    print('FRULA')
else:
    print(''.join(stack))
