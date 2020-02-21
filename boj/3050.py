R, C = map(int, input().split())
M = []
for _ in range(R):
    M.append(input())

mat1 = []
for row in M:
    l1 = []
    count = 0
    for idx, c in enumerate(row):
        if c == 'X':
            count = 0
        else:
            count += 1
        l1.append(count)

    mat1.append(l1)

max_val = 0
for r in range(R):
    for c in range(C):
        right_count = mat1[r][c]

        new_r = r
        while new_r < R and mat1[new_r][c] > 0:
            right_count = min(right_count, mat1[new_r][c])
            max_val = max(max_val, 2*(right_count+(new_r-r+1)))
            new_r += 1
if max_val == 0:
    print(0)
else:
    print(max_val-1)
