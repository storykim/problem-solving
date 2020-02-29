import sys
import collections
input = sys.stdin.readline
n, m = map(int, input().split())
mat = [ input().strip() for _ in range(n) ]

visited = set()
visited.add((0,0,0))

# bfs
q = collections.deque()
q.append((0,0,0,1)) # row, col, break_used, distance

final_dist = -1
while q:
    row, col, break_used, distance = q.popleft()
    if row == n-1 and col == m-1:
        final_dist = distance
        break

    for dr, dc in ((1,0), (0,1), (-1,0), (0,-1)):
        row2, col2 = row+dr, col+dc
        if not (0<=row2<n and 0<=col2<m):
            continue

        if mat[row2][col2] == '1':
            if break_used:
                continue
            if (row2, col2, 1) in visited:
                continue
            visited.add((row2,col2,1))
            q.append((row2,col2,1, distance+1))
        else:
            if (row2, col2, break_used) in visited:
                continue
            visited.add((row2,col2,break_used))
            q.append((row2,col2,break_used, distance+1))
print(final_dist)
