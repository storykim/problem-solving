n = int(input())
pic = [ input() for _ in range(n)]

# count number of specific group
def count(colors):
    visited = set()
    num = 0

    for i in range(n):
        for j in range(n):
            if (i,j) in visited:
                continue
            if pic[i][j] not in colors:
                continue
            num += 1
            # start dfs
            stack = [(i,j)]
            visited.add((i,j))
            while stack:
                point = stack.pop()
                for di, dj in ((1,0), (0,1), (-1,0), (0,-1)):
                    #NOTE: i,j 대신 point! 자주하는 실수
                    i2, j2 = point[0]+di, point[1]+dj
                    if (i2, j2) in visited:
                        continue

                    if not (0<=i2<n and 0<=j2<n):
                        continue

                    if pic[i2][j2] not in colors:
                        continue

                    visited.add((i2,j2))
                    stack.append((i2,j2))
    return num

b_count = count(['B'])
r_count = count(['R'])
g_count = count(['G'])
rg_count = count(['R', 'G'])
print(b_count+r_count+g_count, b_count+rg_count)



    
