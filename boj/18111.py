import sys
input = sys.stdin.readline

r, c, b = map(int, input().split())
mat = []
for _ in range(r):
    mat.append(list(map(int, input().split())))

def calculate_time(desired_h):
    # Assume it is possible to make all cells to height h
    t = 0
    for row in mat:
        for elem in row:
            diff = elem - desired_h
            if diff > 0:
                t += diff * 2
            else:
                # NOTE : diff에 abs 붙이기
                t += abs(diff)
    return t

def calculate_max_height():
    total_blocks = b
    for row in mat:
        for elem in row:
            total_blocks += elem
    return total_blocks // (r*c)

min_time = float('inf')
ans_h = 0
for h in range(0, calculate_max_height() + 1):
    t = calculate_time(h)
    if min_time >= t:
        min_time = t
        ans_h = h
print(min_time, ans_h)

