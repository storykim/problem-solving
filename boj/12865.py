from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
weight = []
value = []
for _ in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

dp = [[0] * (k+1) for _ in range(n)]

def get(i, j):
    if i<0 or j<0:
        return 0
    return dp[i][j]

for i in range(n):
    for j in range(k+1):
        if weight[i] <= j:
            dp[i][j] = max(get(i-1, j), get(i-1, j-weight[i]) + value[i])
        else:
            dp[i][j] = get(i-1, j)

print(dp[-1][-1])
