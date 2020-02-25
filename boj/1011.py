def solve(d):
    i = 0
    while i**2 <= d:
        i+= 1
    i -= 1
    return 2*i-1 + ((d-i**2)-1)//i + 1

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(solve(b-a))

