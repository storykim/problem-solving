import itertools
n, m = map(int, input().split())

mat = []
for _ in range(n):
    mat.append(list(map(int,input().split())))

stores = []
homes = []
for i in range(n):
    for j in range(n):
        if mat[i][j] == 2:
            stores.append((i,j))
        elif mat[i][j] == 1:
            homes.append((i,j))

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def simulate(homes, stores):
    chicken_dist = 0
    for home in homes:
        close = float('inf')
        for store in stores:
            d = distance(home, store)
            close = min(close, d)
        chicken_dist += close
    return chicken_dist

min_dist = float('inf')
for store_combination in itertools.combinations(stores, m):
    min_dist = min(min_dist, simulate(homes, store_combination))

print(min_dist)

