N = int(input())
l = []
for _ in range(N):
    s = input()
    if s == '0':
        l.pop()
    else:
        l.append(int(s))
print(sum(l))
