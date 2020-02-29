from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
mat = [ list(map(int, input().split())) for _ in range(n)]

k = int(input())

# preprocessing
preprocess_sum = []
for i in range(n):
    row = []
    row_sum = 0
    for j in range(m):
        row_sum += mat[i][j]
        if i == 0:
            row.append(row_sum)
        else:
            row.append(row_sum + preprocess_sum[i-1][j])

    preprocess_sum.append(row)

def get_sum(i,j):
    if i<0 or j<0:
        return 0
    return preprocess_sum[i][j]

for _ in range(k):
    i, j, x, y = map(int, input().split())
    i, j, x, y = i-1, j-1, x-1, y-1
    result = get_sum(x,y) + get_sum(i-1, j-1) - (get_sum(i-1, y) + get_sum(x, j-1))
    print(result)
