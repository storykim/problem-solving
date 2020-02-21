def gcd(a,b):
    if a<b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a%b)

n, m = map(int, input().split())
g = gcd(n,m)
print(g)
print(n*m//g)
