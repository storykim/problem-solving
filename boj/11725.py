from sys import stdin
from collections import defaultdict
input = stdin.readline

n = int(input())
edges = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

parents = [None] * (n+1)
parents[0] = parents[1] = 0

stack = [1]
while stack:
    node = stack.pop()
    for child in edges[node]:
        if parents[child] is not None:
            continue

        parents[child] = node
        stack.append(child)

for idx in range(2, n+1):
    print(parents[idx])
