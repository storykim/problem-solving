N, r, c = map(int, input().split())

def solve(n, r, c):
    if n == 1:
        return r*2+c
    else:
        half = 2**(n-1)
        if r >= half and c >= half:
            return 3*2**(2*n-2) + solve(n-1, r-half, c-half)
        elif r >= half:
            return 2*2**(2*n-2) + solve(n-1, r-half, c)
        elif c>=half:
            return 2**(2*n-2) + solve(n-1, r, c-half)
        else:
            return solve(n-1, r, c)

print(solve(N, r, c))
