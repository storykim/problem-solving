from sys import stdin
R, C = map(int, stdin.readline().split())
M = []
for _ in range(R):
    M.append(stdin.readline())

max_size = 1
def valid(r, c):
    return 0<=r<R and 0<=c<C

def calc_max_size(r, c):
    # odd size square
    n = 1
    while valid(r-n, c-n) and valid(r+n, c+n):
        # check boundary
        ok = True
        for i in range(2*n+1):
            if M[r-n+i][c-n] != M[r+n-i][c+n]:
                ok = False
                break
            if M[r-n][c-n+i] != M[r+n][c+n-i]:
                ok = False
                break
        if not ok: break
        n += 1
    ret = 2*(n-1) + 1

    # even size square
    n = 0
    while valid(r-n, c-n) and valid(r+n+1, c+n+1):
        ok = True
        for i in range(2*n+2):
            if M[r-n+i][c-n] != M[r+n+1-i][c+n+1]:
                ok = False
                break
            if M[r-n][c-n+i] != M[r+n+1][c+n+1-i]:
                ok = False
                break
        if not ok: break
        n += 1
    ret = max(ret, 2*n)
    return ret

for r in range(R):
    for c in range(C):
        max_size = max(max_size, calc_max_size(r, c))
print(max_size)
