import sys
input = sys.stdin.readline

def solve():
    r, c, k = map(int, input().split())
    m = [ [0] * c for _ in range(r)]
    for _ in range(k):
        i, j = map(int,input().split())
        m[i][j] = 1

    visited = set()
    count = 0
    for i in range(r):
        for j in range(c):
            if (i,j) in visited or m[i][j] == 0: continue
            # dfs
            count += 1
            stack = [(i,j)]
            visited.add((i,j))
            while stack:
                x, y = stack.pop()
                for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
                    new_x, new_y = x + dx, y + dy
                    if 0<=new_x<r and 0<=new_y<c and m[new_x][new_y] and (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        stack.append((new_x, new_y))
    print(count)

t = int(input())
for _ in range(t):
    solve()
