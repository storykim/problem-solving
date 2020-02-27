import collections
n = int(input())

mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

def get_available_food(cur_pos, cur_level):
    # run dfs
    closest = None
    closest_dist = float('inf')

    q = collections.deque([(cur_pos, 0)])
    visited = set()
    visited.add(cur_pos)
    while q:
        pos, dist = q.popleft()
        if 1 <= mat[pos[0]][pos[1]] < cur_level:
            if dist < closest_dist:
                closest = pos
                closest_dist = dist
            elif dist == closest_dist:
                closest = min(closest, pos)

        for di, dj in ((1,0), (-1,0), (0, -1), (0,1)):
            new_i, new_j = pos[0] + di, pos[1] + dj
            if not (0<=new_i<n and 0<=new_j<n):
                continue
            if (new_i, new_j) in visited:
                continue
            if mat[new_i][new_j] > cur_level:
                continue
            visited.add((new_i, new_j))
            q.append(((new_i, new_j), dist+1))
    return closest, closest_dist

level = 2
feed = 0
def find_cur_pos():
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 9:
                return i, j

cur_pos = find_cur_pos()
mat[cur_pos[0]][cur_pos[1]] = 0
time = 0
while True:
    food, dist = get_available_food(cur_pos, level)
    if food is None:
        break
    time += dist
    feed += 1
    cur_pos = food
    mat[cur_pos[0]][cur_pos[1]] = 0
    
    if feed == level:
        level += 1
        feed = 0

print(time)

