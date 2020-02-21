def check(s):
    count = 0
    for c in s:
        if c == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                return False
    return count == 0

t = int(input())
for _ in range(t):
    print('YES' if check(input()) else 'NO')
