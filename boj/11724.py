import sys, collections
input =sys.stdin.readline

visited = set()
conn = collections.defaultdict(list)

n, m = map(int, input().split())
for _ in range(m):
    u, v = map(int, input().split())
    conn[u].append(v)
    conn[v].append(u)

count = 0
for i in range(1, n+1):
    if i in visited:
        continue

    # dfs
    stack = [i]
    visited.add(i)
    while stack:
        node = stack.pop()

        for neighbor in conn[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    count += 1
print(count)

