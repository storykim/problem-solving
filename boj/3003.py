truth = [1,1,2,2,2,8]
dh = list(map(int, input().split()))
gap = [ elem - dh[i] for i, elem in enumerate(truth) ]
for e in gap:
    print(e, end=' ')
