def solve(s):
    stack = []

    # NOTE: 사이에 끼여있는 것 확인
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack or stack.pop() != '(':
                print('no')
                return
        elif c == '[':
            stack.append(c)
        elif c == ']':
            if not stack or stack.pop() != '[':
                print('no')
                return
        else:
            pass
    print('no' if stack else 'yes')

while True:
    s = input()
    if s == '.':
        break
    solve(s)

