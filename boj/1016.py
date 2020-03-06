import math
MIN, MAX = map(int, input().split())


def solve(MIN, MAX):
    sq = int(math.sqrt(MAX))
    i = 2

    is_ok = [True] * (MAX-MIN+1)
    while i*i <= MAX:
        tmp = i*i
        j = max((MIN-1) // tmp + 1, 1)

        while tmp * j <= MAX:
            is_ok[tmp*j - MIN] = False
            j += 1
        i += 1
    return sum(is_ok)

print(solve(MIN, MAX))

