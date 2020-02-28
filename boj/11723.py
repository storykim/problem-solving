from sys import stdin
input = stdin.readline

S = [0] * 20
M = int(input())
for _ in range(M):
    query = input().strip()
    if query == 'empty':
        for i in range(20):
            S[i] = 0
    elif query == 'all':
        for i in range(20):
            S[i] = 1
    else:
        query, param = query.split()
        param = int(param) - 1
        if query == 'add':
            S[param] = 1
        elif query == 'remove':
            S[param] = 0
        elif query == 'check':
            print(1 if S[param] else 0)
        else:
            S[param] = 0 if S[param] else 1

