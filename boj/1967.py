import sys
import collections
input = sys.stdin.readline
net = collections.defaultdict(dict)

n = int(input())
for _ in range(n-1):
    a, b, w = map(int, input().split())
    net[a][b] = w
    net[b][a] = w

# start from any node, find the farthest one
def find_farthest(start):
    visited = set()
    visited.add(start)
    stack = [(start,0)]
    farthest = start
    far_dist = 0

    while stack:
        node, dist = stack.pop()
        if dist > far_dist:
            far_dist = dist
            farthest = node

        for neighbor, weight in net[node].items():
            if neighbor in visited:
                continue
            visited.add(neighbor)
            stack.append((neighbor, dist + weight))
    return farthest, far_dist

farthest, _ = find_farthest(1)
_, diameter = find_farthest(farthest)
print(diameter)
