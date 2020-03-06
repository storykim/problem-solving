from sys import stdin
from collections import defaultdict
import heapq
input = stdin.readline
n, m, x = map(int, input().split())

forward_edges = defaultdict(dict)
backward_edges = defaultdict(dict)

for _ in range(m):
    start, end, w = map(int, input().split())
    forward_edges[start][end] = w
    backward_edges[end][start] = w

total_dist = [0] * (n+1)
# dijkstra for forward
pq = [(0, x)]
visited = {}
while pq:
    dist, node = heapq.heappop(pq)
    if node in visited:
        continue
    visited[node] = dist
    total_dist[node] += dist

    for nb, w in forward_edges[node].items():
        if nb in visited:
            continue

        heapq.heappush(pq, (dist+w, nb))

# dijkstra for forward
pq = [(0, x)]
visited = {}
while pq:
    dist, node = heapq.heappop(pq)
    if node in visited:
        continue
    visited[node] = dist
    total_dist[node] += dist

    for nb, w in backward_edges[node].items():
        if nb in visited:
            continue

        heapq.heappush(pq, (dist+w, nb))

print(max(total_dist))
