import collections
t = int(input())

for _ in range(t):
    d = collections.defaultdict(int)
    n = int(input())
    for _ in range(n):
        _, cat = input().split()
        d[cat] += 1
    days = 1
    for _, v in d.items():
        days *= (v+1)
    print(days-1)

