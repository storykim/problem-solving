from collections import deque
start, end = map(int, input().split())

# bfs
q = deque()
q.append((start, 1))

visited = set()
val = -1
while q:
    num, dist = q.popleft()
    if num == end:
        val = dist
        break

    for next_num in (2*num, num*10 + 1):
        if next_num > 1000000000:
            continue
        if next_num in visited:
            continue
        visited.add(next_num)
        q.append((next_num, dist+1))
print(val)
