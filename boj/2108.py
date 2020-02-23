import sys
import collections
N = int(sys.stdin.readline())
l = []
for _ in range(N):
    l.append(int(sys.stdin.readline()))

l.sort()

print(int(round(sum(l)/N, 0)))
print(l[N//2])
if N == 1:
    print(l[0])
else:
    c = collections.Counter(l)
    cl = c.most_common()
    cl.sort(key=lambda e: (-e[1], e[0]))
    if cl[0][1] == cl[1][1]:
        print(cl[1][0])
    else:
        print(cl[0][0])
print(l[-1] - l[0])
