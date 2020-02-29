from collections import deque
input()
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

dq = deque()
dq.append((inorder, postorder))

while dq:
    i, p = dq.popleft()
    if len(p) == 1:
        print(p[0], end=' ')
        continue
    elif len(p) == 0:
        continue

    root = p[-1]
    print(root, end=' ')

    idx = i.index(root)
    dq.appendleft((i[idx+1:], p[idx:-1]))
    dq.appendleft((i[:idx], p[:idx]))

