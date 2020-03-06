from sys import stdin
from collections import defaultdict
import heapq

input = stdin.readline
n, e = map(int, input().split())
edges = defaultdict(dict)

for _ in range(e):
    s, e, c = map(int, input().split())
    s, e = s-1, e-1

    edges[s][e] = min(edges[s][e], c) if e in edges[s] else c
    edges[e][s] = min(edges[e][s], c) if s in edges[e] else c
visit1, visit2 = map(int, input().split())
visit1 -= 1
visit2 -= 1

dist_from_start = [float('inf')] * n
dist_from_visit1 = [float('inf')] * n
dist_from_visit2 = [float('inf')] * n

def dijkstra(start, dist_list):
    visited = set()
    pq = [(0, start)]

    # NOTE : dist_list[start] 0으로 바꾸는거 while 안에서 해야함
    #dist_list[start] = 0

    while pq:
        dist, node = heapq.heappop(pq)
        if dist_list[node] < float('inf'):
            continue
        dist_list[node] = dist
        for next_node, weight in edges[node].items():
            if dist_list[next_node] < float('inf'):
                continue
            heapq.heappush(pq, (dist + weight, next_node))
    return

dijkstra(0, dist_from_start)
dijkstra(visit1, dist_from_visit1)
dijkstra(visit2, dist_from_visit2)

min_dist = min(
        dist_from_start[visit1] + dist_from_visit1[visit2] + dist_from_visit2[-1],
        dist_from_start[visit2] + dist_from_visit2[visit1] + dist_from_visit1[-1]
        )
print(min_dist if min_dist < float('inf') else -1)
