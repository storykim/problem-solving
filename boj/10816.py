import collections
input()
c = collections.Counter(map(int, input().split()))
input()
q = list(map(int, input().split()))
for elem in q:
    print(c[elem], end=' ')
