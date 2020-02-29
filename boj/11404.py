import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dist = [ [float('inf')] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    # NOTE: 중복 체크
    s, e, d = map(int, input().split())
    dist[s-1][e-1] = min(d, dist[s-1][e-1])

for mid in range(n):
    for start in range(n):
        for end in range(n):
            dist[start][end] = min(dist[start][end], dist[start][mid] + dist[mid][end])

for i in range(n):
    for j in range(n):
        d = dist[i][j]
        print(d if d < float('inf') else 0, end=' ')
    print()

