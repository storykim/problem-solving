import sys
k, n = map(int, sys.stdin.readline().split())
l = []
for _ in range(k):
    l.append(int(sys.stdin.readline()))

def check(length):
    count = 0
    for elem in l:
        count += elem // length

    return count >= n

low = 0
hi = (2**31)
while low < hi:
    mid = (low + hi) // 2
    if check(mid):
        low = mid + 1
    else:
        hi = mid

print(hi-1)
