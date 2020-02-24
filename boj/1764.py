import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s1 = set()
s2 = set()
for _ in range(n):
    s1.add(input().strip())
for _ in range(m):
    s2.add(input().strip())
l = sorted(list(s1.intersection(s2)))
print(len(l))
print('\n'.join(l))

