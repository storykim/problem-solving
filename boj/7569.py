import sys
import collections
input = sys.stdin.readline

c, r, h = map(int, input().split())
box = []

for _ in range(h):
    one_layer = []
    for _ in range(r):
        one_layer.append(list(map(int, input().split())))

    box.append(one_layer)

# box : h x r x c list
longest = 0
q = collections.deque()
visited = set()
for i in range(h):
    for j in range(r):
        for k in range(c):
            if box[i][j][k] == 1:
                q.append((i,j,k, 0))
                visited.add((i,j,k))

# check the distance btw 1 and 0
while q:
    i, j, k, dist = q.popleft()
    longest = max(longest, dist)

    for di, dj, dk in ((1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)):
        i2, j2, k2 = i+di, j+dj, k+dk
        if (i2, j2, k2) not in visited and 0<=i2<h and 0<=j2<r and 0<=k2<c and box[i2][j2][k2] == 0:
            q.append((i2,j2,k2, dist+1))
            visited.add((i2,j2,k2))

# check if all 0 is visited
def check_all_visited():
    for i in range(h):
        for j in range(r):
            for k in range(c):
                if box[i][j][k] == 0 and (i,j,k) not in visited:
                    return False
    return True

if check_all_visited():
    print(longest)
else:
    print(-1)
