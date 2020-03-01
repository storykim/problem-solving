from sys import stdin
input = stdin.readline

def solve():
    n, m = map(int, input().split())
    if n == 1 and m == 0:
        return 0
    digits = [None] * n

    for _ in range(m):
        s, c = map(int, input().split())
        s -= 1
        if digits[s] is None or digits[s] == c:
            digits[s] = c
        else:
            return -1

    num = 0
    if digits[0] == 0:
        if len(digits) == 1:
            return 0
        else:
            return -1

    for idx, digit in enumerate(digits):
        if digit is None:
            if idx == 0:
                digit = 1
            else:
                digit = 0
        num = num * 10 + digit
    return num

print(solve())

