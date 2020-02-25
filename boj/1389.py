import sys
import collections
input = sys.stdin.readline

n, m = map(int, input().split())
net = collections.defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

min_person = -1
min_count = float('inf')

for i in range(1, n+1):
    # run BFS
    visited = set()
    visited.add(i)
    q = collections.deque()
    q.append((i,0))
    count = 0

    while q:
        person, distance = q.popleft()
        count += distance

        for neighbor in net[person]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append((neighbor, distance+1))
    if count < min_count:
        min_count = count
        min_person = i
print(min_person)

