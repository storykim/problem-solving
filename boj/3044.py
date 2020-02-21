import collections
import sys
n, m = map(int, sys.stdin.readline().split())

# NOTE : add one by one
# NOTE : print inf only if there exists route to 1
routes = []
for _ in range(n):
    routes.append(collections.defaultdict(int))

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    start = start - 1
    end = end - 1
    routes[start][end] += 1

def check_cycle():
    visited = set()
    visited.add(0)
    rec_stack = set()
    rec_stack.add(0)

    def dfs(cur_city):
        for next_city in routes[cur_city]:
            if next_city in rec_stack:
                return True # cycle found
            elif next_city not in visited:
                visited.add(next_city)
                rec_stack.add(next_city)
                if dfs(next_city) == True:
                    return True
                rec_stack.remove(next_city)
        return False
    return dfs(0)

def reach_dest():
    q = collections.deque()
    q.append(0)
    visited = set()
    visited.add(0)
    while q:
        cur_city = q.popleft()
        for next_city in routes[cur_city]:
            if next_city in visited: continue
            visited.add(next_city)
            q.append(next_city)
    return 1 in visited
    
def find_routes():
    cur_set = {0: 1} # city : num routes
    next_set = collections.defaultdict(int)
    ret = 0
    while cur_set:
        for city in cur_set:
            if city == 1:
                ret += cur_set[city]

            for next_city in routes[city]:
                next_set[next_city] += cur_set[city] * routes[city][next_city]

        cur_set = next_set
        next_set = collections.defaultdict(int)
    return ret

if not reach_dest():
    print(0)
if check_cycle():
    print(float('inf'))
else:
    print(str(find_routes())[-9:])
