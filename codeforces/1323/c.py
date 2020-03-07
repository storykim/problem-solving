input()
s = input()

count = 0
ans = 0

length = 0

for c in s:
    if c == '(':
        count += 1
        length += 1
        if count == 0:
            ans += length
            length = 0
    else:
        count -= 1
        length += 1
        if count == 0:
            length = 0
print(ans if count == 0 else -1)
