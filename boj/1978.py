sieve = [True] * 1001
sieve[0] = False
sieve[1] = False

i = 2
while i**2 <= 1000:
    if sieve[i]:
        j = 2
        while i*j <= 1000:
            sieve[i*j] = False
            j += 1
    i+=1

N = int(input())
l = map(int, input().split())
l = [sieve[elem] for elem in l]
print(sum(l))
