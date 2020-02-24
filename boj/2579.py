import sys
input = sys.stdin.readline

n = int(input())

scores = []
for _ in range(n):
    scores.append(int(input()))

arr = [ [0,0] for _ in range(n+1) ]
arr[1] = [scores[0], scores[0]]

for i in range(2, n+1):
    arr[i][0] = max(arr[i-2]) + scores[i-1]
    arr[i][1] = arr[i-1][0] + scores[i-1]

print(max(arr[-1]))

