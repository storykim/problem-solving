import collections

def solve():
    start, end = map(int, input().split())
    if start == end:
        return 0

    dq = collections.deque()
    visited = set()
    visited.add(start)
    dq.append((start, 0))

    while dq:
        num, time = dq.popleft()

        if num*2 <= 100000 and num*2 not in visited:
            visited.add(num*2)
            if num*2 == end:
                return time
            dq.appendleft((num*2, time))

        if num-1 >= 0 and num-1 not in visited:
            visited.add(num-1)
            if num-1 == end:
                return time+1
            dq.append((num-1, time+1))

        if num+1 <= 100000 and num+1 not in visited:
            visited.add(num+1)
            if num+1 == end:
                return time+1
            dq.append((num+1, time+1))

print(solve())
