a,b,c = map(int, input().split())
def power(a, b, c):
    if b == 0:
        return 1
    half = power(a, b//2, c)
    if b % 2:
        return half * half * a % c
    else:
        return half * half % c
print(power(a,b,c))
