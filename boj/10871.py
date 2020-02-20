import sys
_, k = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
for elem in l:
    if elem < k:
        print(elem, end= ' ')
