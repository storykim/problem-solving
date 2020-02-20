s = set(range(1,10001))

def d(num):
    ret = num
    while num:
        ret += num % 10
        num //= 10
    return ret

for num in range(1, 10001):
    gen_num = d(num)
    if gen_num in s:
        s.remove(gen_num)

l = sorted(list(s))
for elem in l:
    print(elem)

