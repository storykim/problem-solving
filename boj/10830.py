n, b = map(int, input().split())
mat = [ list(map(int, input().split())) for _ in range(n)]

def multiply(a, b):
    n = len(a)
    new = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                new[i][j] += a[i][k] * b[k][j]
            new[i][j] %= 1000
    return new

def pow(a, b):
    if b == 1:
        return a
    half = pow(a, b//2)
    ret = multiply(half, half)
    if b%2:
        ret = multiply(ret, a)
    return ret

result = pow(mat, b)
for row in result:
    for col in row:
        print(col%1000, end=' ')
    print()

