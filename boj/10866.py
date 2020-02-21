import collections
import sys
s = collections.deque()

n = int(sys.stdin.readline())
for _ in range(n):
    cmd = sys.stdin.readline().strip()
    if cmd == "front":
        print(s[0] if s else -1)
    elif cmd == "back":
        print(s[-1] if s else -1)
    elif cmd == "empty":
        print(0 if s else 1)
    elif cmd == "size":
        print(len(s))
    elif cmd == "pop_front":
        print(s.popleft() if s else -1)
    elif cmd == "pop_back":
        print(s.pop() if s else -1)
    elif cmd.startswith('push_front'):
        _, x = cmd.split()
        s.appendleft(x)
    else:
        _, x = cmd.split()
        s.append(x)
