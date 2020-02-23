m, n = map(int, input().split())
cieve = [True] * (n+1)
cieve[0] = False
if len(cieve) >= 2:
    cieve[1] = False

i = 2
while i*i <= n:
    if cieve[i]:
        k = 2
        while i*k <= n:
            cieve[i*k] = False
            k += 1
    i += 1

for i in range(m, n+1):
    if cieve[i]:
        print(i)
