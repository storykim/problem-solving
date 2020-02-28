import bisect

def solve(l):
    q = []
    for elem in l:
        idx = bisect.bisect_left(q, elem)
        if idx == len(q):
            q.append(elem)
        else:
            q[idx] = elem
    return len(q)

input()
ans = solve(list(map(int, input().split())))
print(ans)
