n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins = coins[::-1]

count = 0
for coin in coins:
    count += k // coin
    k %= coin
print(count)
