import sys
import collections
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())

net = collections.defaultdict(dict)
for _ in range(m):
    a, b, w = map(int, input().split())
    # NOTE: 간선 무게 다른거 여러개 있을 때 중복체크
    if b in net[a]:
        net[a][b] = min(w, net[a][b])
    else:
        net[a][b] = w

start, end = map(int, input().split())
pq = [(0, start)]

visited = set()
while pq:
    # NOTE: heapq 쓸 때 tuple 넣을거면 소트 잘 확인
    dist, city = heapq.heappop(pq)
    if city in visited:
        continue
    visited.add(city)
    if city == end:
        print(dist)
        break

    for neighbor, dist2 in net[city].items():
        if neighbor in visited:
            continue
        heapq.heappush(pq, (dist + dist2, neighbor))
