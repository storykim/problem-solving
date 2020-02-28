n, m = map(int, input().split())

def fac(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret

print(fac(n) // (fac(m) * fac(n-m)  ))
