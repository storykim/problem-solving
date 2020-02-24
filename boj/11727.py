n = int(input())
if n == 1: print(1)
elif n == 2: print(3)
else:
    prev1, prev2 = 1, 3
    for i in range(3, n+1):
        prev1, prev2 = prev2, 2*prev1 + prev2

    print(prev2 % 10007)
