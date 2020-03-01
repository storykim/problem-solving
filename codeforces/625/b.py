from sys import stdin
input = stdin.readline

n = int(input())
l = list(map(int, input().split()))

cache = [None] * n

max_val = 0
last_diff = {}

for i in range(n-1, -1, -1):
    ret = l[i]
    if i-l[i] in last_diff:
        idx = last_diff[i-l[i]]
        ret += cache[idx]

    cache[i] = ret
    max_val = max(max_val, ret)
    last_diff[i-l[i]] = i
print(max_val)
