import collections

def solve(start, end):
    if start == end:
        return 0, {start:None}

    dq = collections.deque()
    visited = {}
    visited[start] = None
    dq.append((start, 0))

    while dq:
        num, time = dq.popleft()

        if num*2 <= 100000 and num*2 not in visited:
            visited[num*2] = num
            if num*2 == end:
                return time+1, visited
            dq.append((num*2, time+1))

        if num-1 >= 0 and num-1 not in visited:
            visited[num-1] = num
            if num-1 == end:
                return time+1, visited
            dq.append((num-1, time+1))

        if num+1 <= 100000 and num+1 not in visited:
            visited[num+1] = num
            if num+1 == end:
                return time+1, visited
            dq.append((num+1, time+1))

start, end = map(int, input().split())
t, visited = solve(start, end)
print(t)
path = []
while end is not None:
    path.append(end)
    end = visited[end]

for elem in path[::-1]:
    print(elem, end=' ')
