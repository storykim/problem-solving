input()
a = reversed(input())
b = input()
l = []
for c in a:
    l.append((c, 0))
for c in b:
    l.append((c, 1))

t = int(input())
for _ in range(t):
    idx = 0
    while idx < len(l) - 1:
        elem = l[idx]
        if elem[1] == 1:
            idx += 1
            continue
        
        if l[idx+1][1] == 1:
            l[idx], l[idx+1] = l[idx+1], l[idx]
            idx += 2
        else:
            idx += 1

for elem in l:
    print(elem[0], end='')
