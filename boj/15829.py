def hash(s):
    ret = 0
    for i, c in enumerate(s):
        ret += 31**i * (ord(c) - ord('a') + 1)
        ret %= 1234567891
    return ret % 1234567891
input()
print(hash(input()))

