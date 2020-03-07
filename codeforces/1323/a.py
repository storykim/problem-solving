t = int(input())

def solve():
    n = int(input())
    l = list(map(int, input().split()))

    if len(l) == 1 and l[0] %2:
        print(-1)
        return

    for idx, elem in enumerate(l):
        if elem %2 == 0:
            print(1)
            print(idx+1)
            return
    
    print(2)
    print(1, 2)
    return

for _ in range(t):
    solve()
