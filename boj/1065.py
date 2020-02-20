def is_han(num):
    if num < 100: return True
    diff = num % 10 - (num // 10) % 10

    while num > 9:
        if num % 10 - (num // 10) % 10 != diff:
            return False
        num //= 10
    return True

count = 0
for i in range(1, int(input()) + 1):
    if is_han(i): count += 1
print(count)
