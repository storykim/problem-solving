n = int(input())
fib_count = [None] * (41)
fib_count[0] = (1, 0)
fib_count[1] = (0, 1)
for i in range(2, 41):
    fib_count[i] = (fib_count[i-1][0] + fib_count[i-2][0], fib_count[i-1][1] + fib_count[i-2][1])

for _ in range(n):
    t = int(input())
    print(fib_count[t][0], fib_count[t][1])
