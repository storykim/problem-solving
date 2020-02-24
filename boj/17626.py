squares = [ i ** 2 for i in range(1, 224) ]

n = int(input())
def solve(n):
    if n in squares : return 1

    # k = 2 case
    for i, a in enumerate(squares):
        for j in range(i, len(squares)):
            if a + squares[j] == n:
                return 2

    # k = 3 case
    for i, a in enumerate(squares):
        for j in range(i, len(squares)):
            for k in range(j, len(squares)):
                if a + squares[j] + squares[k] == n:
                    return 3

    return 4

print(solve(n))
