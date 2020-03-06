import collections

def solve():
    start, end = map(int, input().split())
    if start == end:
        return 0, 1

    visited = set()
    visited.add(start)

    cur_map = {start:1}
    next_map = collections.defaultdict(int)
    t = 0
    while True:
        t += 1
        for num, count in cur_map.items():
            if num*2 <= 100000 and num*2 not in visited:
                next_map[num*2] += count

            if num-1 >= 0 and num-1 not in visited:
                next_map[num-1] += count

            if num+1 <= 100000 and num+1 not in visited:
                next_map[num+1] += count

        for key in next_map:
            if key == end:
                return t, next_map[key]

            visited.add(key)
        cur_map = next_map
        next_map = collections.defaultdict(int)

t, count = solve()
print(t)
print(count)
