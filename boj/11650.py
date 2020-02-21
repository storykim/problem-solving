import sys
n = int(sys.stdin.readline())
l = []
for _ in range(n):
    l.append(tuple(map(int, sys.stdin.readline().split())))
l.sort()
for elem in l:
    print(elem[0], elem[1])
