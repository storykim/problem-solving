import collections
import sys
s = collections.deque()

n = int(sys.stdin.readline())
for _ in range(n):
    cmd = sys.stdin.readline().strip()
    if cmd == "top":
        print(s[-1] if s else -1)
    elif cmd == "empty":
        print(0 if s else 1)
    elif cmd == "size":
        print(len(s))
    elif cmd == "pop":
        print(s.pop() if s else -1)
    else:
        _, x = cmd.split()
        s.append(x)
