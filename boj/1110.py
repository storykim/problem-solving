n = int(input())
count = 0

num = n
while True:
    count += 1
    if num < 10:
        num *= 11
    else:
        fst = num // 10
        snd = num % 10
        num = snd * 10 + (fst + snd) % 10

    if num == n:
        break
print(count)
