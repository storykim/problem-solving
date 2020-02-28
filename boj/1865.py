from sys import stdin
input = stdin.readline

def bellman_from_src(src, edges, n):
    # return True if graph contains negative cycle
    dist = [float('inf')] * (n+1)
    dist[src] = 0

    for _ in range(n-1):
        for s, e, d in edges:
            dist[e] = min(dist[e], dist[s] + d)

    # run one more time and check updated
    for s, e, d in edges:
        if dist[e] > dist[s] + d:
            return True
    return False

def solve():
    n, m, w = map(int, input().split())
    edges = []

    for _ in range(m):
        s, e, d = map(int, input().split())
        edges.append((s,e,d))
        edges.append((e,s,d))

    for _ in range(w):
        s, e, d = map(int, input().split())
        edges.append((s,e,-d))

    return bellman_from_src(1, edges, n)

TC = int(input())
for _ in range(TC):
    print('YES' if solve() else 'NO')
