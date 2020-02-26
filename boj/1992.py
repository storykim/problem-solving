n = int(input())
m = []
for _ in range(n):
    m.append(input())

def solve(r, c, n):
    base = m[r][c]
    ok = True
    for dr in range(n):
        for dc in range(n):
            if base != m[r+dr][c+dc]:
                ok = False
                break
        if not ok:
            break

    if not ok:
        half = n//2
        return '(' + solve(r,c,half) + solve(r, c+half, half) + solve(r+half, c, half) + solve(r+half, c+half, half) + ')'
    else:
        return base

print(solve(0, 0, n))

