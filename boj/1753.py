import heapq
from sys import stdin
import collections

input = stdin.readline

v, e = map(int, input().split())
start = int(input())
edges = collections.defaultdict(list)

for _ in range(e):
    s, e, w = map(int, input().split())
    edges[s].append((e, w))

pq = [(0, start)]
distance = [None] * (v+1)

while pq:
    dist, node = heapq.heappop(pq)
    if distance[node] is not None:
        continue
    distance[node] = dist

    for nb, dist_from_node in edges[node]:
        if distance[nb] is not None:
            continue
        new_dist = dist + dist_from_node
        heapq.heappush(pq, (new_dist, nb))

for i in range(1, v+1):
    print(distance[i] if distance[i] is not None else 'INF')



