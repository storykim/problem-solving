import sys
import collections
input = sys.stdin.readline


def simulate(f, l):
    q = collections.deque(l)
    mode = 'front'
    for c in f:
        if c == 'R':
            mode = 'back' if mode == 'front' else 'front'
        else:
            if not q:
                print('error')
                return

            if mode == 'front':
                q.popleft()
            else:
                q.pop()
    l = list(q)
    if mode == 'back':
        l = l[::-1]

    print( '[' + ','.join(l) + ']')
    return

def parse_list(s):
    if len(s)==2: return []
    return s[1:-1].split(',')

t = int(input())
for _ in range(t):
    f = input().strip()
    input()
    l = parse_list(input().strip())
    simulate(f, l)
