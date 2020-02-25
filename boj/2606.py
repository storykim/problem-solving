import sys
import collections
input = sys.stdin.readline

n = int(input())
m = int(input())
network = collections.defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

visited = set()
stack = [1]
visited.add(1)

while stack:
    node = stack.pop()

    for neighbor in network[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            stack.append(neighbor)
print(len(visited) - 1)
