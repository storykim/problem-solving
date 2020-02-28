import collections
def D(num):
    return 2*num%10000

def S(num):
    return (num-1)%10000

def L(num):
    return (num*10 + num//1000) % 10000

def R(num):
    return num//10 + num%10 * 1000

str_to_func = {
    'D': D,
    'S': S,
    'L': L,
    'R': R,
}

t = int(input())
def solve():
    visited = set()
    start, end = map(int, input().split())

    visited.add(start)
    q = collections.deque()
    q.append((start, ''))

    while q:
        cur_value, cur_str = q.popleft()
        for key, func in str_to_func.items():
            next_value = func(cur_value)
            if next_value in visited:
                continue
            if next_value == end:
                return cur_str + key
            visited.add(next_value)
            q.append((next_value, cur_str + key))

for _ in range(t):
    print(solve())
