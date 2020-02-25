import sys
input = sys.stdin.readline

n = int(input())

def gcd(a,b):
    if a > b:
        return gcd(b, a)
    if a == 0:
        return b
    return gcd(b%a, a)

def solve():
    M, N, x, y = map(int, input().split())

    lcm = M*N // gcd(M, N)

    x_list = set()
    y_list = set()

    i = 0
    while x + i*M <= lcm:
        x_list.add(x+i*M)
        i += 1
    i = 0
    while y + i*N <= lcm:
        y_list.add(y+i*N)
        i += 1
    intersect = x_list.intersection(y_list)
    if intersect:
        print(intersect.pop())
    else:
        print(-1)

for _ in range(n):
    solve()
