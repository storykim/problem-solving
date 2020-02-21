l = sorted(list(map(int, input().split())))
s = input()
for c in s:
    print(l[ord(c) - ord('A')], end=' ')
