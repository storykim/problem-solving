import sys
import collections
input = sys.stdin.readline
net = collections.defaultdict(dict)

n = int(input())
for _ in range(n):
    l = list(map(int, input().split()))
    src = l[0]
    l = l[1:-1]
    idx = 0
    while idx < len(l):
        dst, weight = l[idx], l[idx+1]
        net[src][dst] = weight
        idx += 2

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
