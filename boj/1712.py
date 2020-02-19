A, B, C = map(int, input().split())
P = C-B
if P <= 0: print(-1)
else:
    print(A//P+1)
