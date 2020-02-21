N, K = map(int, input().split())
l = list(range(1,N+1))

idx = 0
s = '<'
ret = []
while l:
    idx += K-1
    idx %= len(l)
    ret.append(str(l[idx]))
    l.pop(idx)
print('<'+', '.join(ret)+'>')
