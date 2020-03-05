from sys import stdin
from collections import defaultdict, deque
input = stdin.readline

n, m = map(int, input().split())
edges = defaultdict(list)
forward = defaultdict(list)
for _ in range(m):
    end, start = map(int, input().split())
    edges[start].append(end)
    forward[end].append(start)

k = int(input())
path = list(map(int, input().split()))
start, end = path[0], path[-1]

# bfs from end
dist = {end:0}
q = deque()
q.append(end)

while q:
    node = q.popleft()

    for nb in edges[node]:
        if nb in dist:
            continue
        dist[nb] = dist[node] + 1
        q.append(nb)

# iterate
MIN, MAX = 0, 0
for idx in range(k):
    if idx == k - 1:
        break
    now = path[idx]
    next_node = path[idx+1]

    if dist[next_node] + 1 != dist[now]:
        MIN += 1
        MAX += 1
    elif any( dist[child] + 1 == dist[now] for child in forward[now] if child != next_node):
        MAX += 1
print(MIN, MAX)

