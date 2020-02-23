import sys
input = sys.stdin.readline
n = int(input())
popped = 0

stack = []
next_num = 1

ret = ''
for _ in range(n):
    next_output = int(input())
    if popped < next_output:
        # push until next_output
        if next_num > next_output:
            ret = 'NO'
            break
        else:
            while next_num <= next_output:
                stack.append(next_num)
                next_num += 1
                ret += '+\n'
            # pop
            popped = stack.pop()
            ret += '-\n'
    else:
        # check top of the stack
        if not stack:
            ret = 'NO'
            break
        elif stack[-1] != next_output:
            ret = 'NO'
            break
        else:
            popped = stack.pop()
            ret += '-\n'
print(ret)
