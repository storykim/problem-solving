n = int(input())
input()
s = input()

count = 0
idx = 0
while idx < len(s)-2:
    if s[idx] == 'O':
        idx += 1
        continue

    o_count = 0
    while idx < len(s)-2 and s[idx+1] == 'O' and s[idx+2] == 'I':
        o_count += 1
        idx += 2

        if o_count == n:
            o_count -= 1
            count += 1
    idx += 1
print(count)
