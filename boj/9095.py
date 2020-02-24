count = [None] * 11
count[0] = 1
count[1] = 1
count[2] = 2

def solve(num):
    if count[num] is not None:
        return count[num]

    counter = solve(num-3) + solve(num-2) + solve(num-1)
    return counter

T = int(input())
for _ in range(T):
    print(solve(int(input())))

