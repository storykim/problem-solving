from sys import stdin
input = stdin.readline

n = int(input())
cost = [ list(map(int, input().split())) for _ in range(n) ]

cost_until = [ [0,0,0] for _ in range(n)]
cost_until[0] = cost[0]

for i in range(1, n):
    cost_until[i][0] = cost[i][0] + min(cost_until[i-1][1], cost_until[i-1][2])
    cost_until[i][1] = cost[i][1] + min(cost_until[i-1][0], cost_until[i-1][2])
    cost_until[i][2] = cost[i][2] + min(cost_until[i-1][0], cost_until[i-1][1])

print(min(cost_until[-1]))
