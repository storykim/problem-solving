n = int(input())
if n == 1: print(1)
elif n == 2: print(2)
else:
    prev1, prev2 = 1, 2
    for i in range(3, n+1):
        prev1, prev2 = prev2, prev1 + prev2

    print(prev2 % 10007)
