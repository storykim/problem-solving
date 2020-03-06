n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n) ]

def idx_to_ij(idx):
    return idx//m, idx%m

def check():
    # return area of safe region
    stack = []
    visited = set()
    num_wall = 0

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                num_wall += 1
            elif mat[i][j] == 2:
                stack.append((i,j))
                visited.add((i,j))

    while stack:
        i,j = stack.pop()
        for di, dj in ((1,0), (0,1), (-1,0), (0,-1)):
            i2, j2 = i+di, j+dj
            if not (0<=i2<n and 0<=j2<m):
                continue
            if (i2, j2) in visited:
                continue
            # NOTE : 벽에 가로막히도록 구현
            if mat[i2][j2] == 1:
                continue
            visited.add((i2,j2))
            stack.append((i2,j2))
    return n*m - len(visited) - num_wall

max_area = 0
for i in range(n*m):
    i1, j1 = idx_to_ij(i)
    if mat[i1][j1] != 0: continue
    mat[i1][j1] = 1
    for j in range(i+1, n*m):
        i2, j2 = idx_to_ij(j)
        if mat[i2][j2] != 0: continue
        mat[i2][j2] = 1
        for k in range(j+1, n*m):
            i3, j3 = idx_to_ij(k)
            if mat[i3][j3] != 0: continue
            mat[i3][j3] = 1
            max_area = max(max_area, check())
            mat[i3][j3] = 0

        mat[i2][j2] = 0

    mat[i1][j1] = 0

print(max_area)

