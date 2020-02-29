import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = list(map(int, input().split()))

route = [ [float('inf')] * n for _ in range(n) ]
for i in range(n):
    route[i][i] = 0

for _ in range(r):
    s, e, d = map(int, input().split())
    # NOTE : 1부터 시작하는 노드 받을 때 -1 해주기
    route[s-1][e-1] = d
    route[e-1][s-1] = d

for mid in range(n):
    for start in range(n):
        for end in range(n):
            route[start][end] = min(route[start][end], route[start][mid] + route[mid][end])

max_item = 0
for row in route:
    item = 0
    for idx, dest in enumerate(row):
        if dest <= m:
            item += items[idx]
    max_item = max(item, max_item)
print(max_item)
