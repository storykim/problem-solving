from sys import stdin
from collections import defaultdict
input = stdin.readline

n,m,k = map(int, input().split())
net = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

blocks = [ tuple(map(int, input().split())) for _ in range(k)]
id_to_group = {}
groups = []
num_candid = [0] * (n+1)

group_id = -1
for start in range(1, n+1):
    if start in id_to_group:
        continue
    group_id += 1
    # search connected component
    group = set()
    stack = [start]
    group.add(start)
    id_to_group[start] = group_id

    while stack:
        node = stack.pop()
        for nb in net[node]:
            if nb in id_to_group:
                continue
            group.add(nb)
            id_to_group[nb] = group_id
            stack.append(nb)
    for member in group:
        num_candid[member] = len(group) - 1 - len(net[member])

# deal with blcok
for a,b in blocks:
    if id_to_group[a] == id_to_group[b]:
        num_candid[a] -= 1
        num_candid[b] -= 1

for i in range(1, n+1):
    print(num_candid[i], end=' ')

