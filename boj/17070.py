n = int(input())
input_map = [ list(map(int, input().split())) for _ in range(n) ]

count = [ [[0, 0, 0] for _ in range(n)] for _ in range(n) ]
count[0][1][0] = 1

def valid(i, j):
    return 0<=i<n and 0<=j<n and input_map[i][j] == 0

for i in range(n):
    for j in range(n):
        if not valid(i,j): continue

        # type 0
        # NOTE : overwrite 해서 dp init해둔거 사라지는 현상 조심
        if valid(i, j-1):
            count[i][j][0] += count[i][j-1][0] + count[i][j-1][1]

        if valid(i-1, j):
            count[i][j][2] += count[i-1][j][2] + count[i-1][j][1]

        if valid(i, j-1) and valid(i-1, j) and valid(i-1, j-1):
            count[i][j][1] += sum(count[i-1][j-1])

print(sum(count[-1][-1]))
