def is_larger_than_me(you, me):
    return you[0] > me[0] and you[1] > me[1]

N = int(input())
l = []
for _ in range(N):
    l.append(tuple(map(int, input().split())))

for idx in range(N):
    rank = 1
    for idx2 in range(N):
        if idx == idx2: continue
        if is_larger_than_me(l[idx2], l[idx]): rank += 1
    print(rank, end=' ')
